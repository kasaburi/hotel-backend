from sqlalchemy import text

from app.database import SessionLocal

from app.models.hotel import Hotel
from app.models.room import Room
from app.models.room_type import RoomType
from app.models.hotel_image import HotelImage


db = SessionLocal()


# =========================================================
# HELPER - ADD ROOM
# =========================================================

def add_rooms(
    hotel_id,
    room_type_id,
    name_ka,
    name_en,
    description_ka,
    description_en,
    price,
    max_guests,
    quantity
):
    rooms = []

    for _ in range(quantity):
        room = Room(
            hotel_id=hotel_id,
            room_type_id=room_type_id,

            name_ka=name_ka,
            name_en=name_en,

            description_ka=description_ka,
            description_en=description_en,

            price_per_night=price,
            max_guests=max_guests,
            reservation_count=0
        )

        db.add(room)
        rooms.append(room)

    db.flush()

    return rooms


# =========================================================
# HELPER - ADD ROOM TYPE IMAGES
# =========================================================

def add_room_type_images(
    hotel_id,
    room_type_id,
    image_urls
):
    for image_url in image_urls:
        db.execute(
            text("""
                INSERT INTO room_type_images
                (hotel_id, room_type_id, source)
                VALUES (:hotel_id, :room_type_id, :source)
            """),
            {
                "hotel_id": hotel_id,
                "room_type_id": room_type_id,
                "source": image_url
            }
        )


try:

    # =========================================================
    # CLEAN OLD DATA
    # =========================================================

    print("Cleaning old hotel/room data...")

    # ძველი ოთახის ფოტოები აღარ გვჭირდება
    db.execute(text("DELETE FROM room_images"))

    # ახალი room_type_images-ის ძველი მონაცემები
    db.execute(text("DELETE FROM room_type_images"))

    # სასტუმროს ფოტოები
    db.execute(text("DELETE FROM hotel_images"))

    # ოთახები
    db.execute(text("DELETE FROM rooms"))

    # სასტუმროები
    db.execute(text("DELETE FROM hotels"))

    # ოთახის ტიპები
    db.execute(text("DELETE FROM room_types"))

    db.commit()

    print("Old data cleaned successfully.")


    # =========================================================
    # ROOM TYPES
    # =========================================================

    standard_type = RoomType(
        name_ka="სტანდარტული ოთახი",
        name_en="Standard Room"
    )

    deluxe_type = RoomType(
        name_ka="დელუქს ოთახი",
        name_en="Deluxe Room"
    )

    suite_type = RoomType(
        name_ka="ლუქსი",
        name_en="Suite"
    )

    family_type = RoomType(
        name_ka="ოჯახური ოთახი",
        name_en="Family Room"
    )

    single_type = RoomType(
        name_ka="ერთადგილიანი ოთახი",
        name_en="Single Room"
    )

    db.add_all([
        standard_type,
        deluxe_type,
        suite_type,
        family_type,
        single_type
    ])

    db.flush()


    # =========================================================
    # =========================================================
    # HOTEL 1 - RADISSON BLU IVERIA
    # =========================================================
    # =========================================================

    hotel1 = Hotel(
        name_ka="რადისონ ბლუ ივერია",
        name_en="Radisson Blu Iveria Hotel",

        description_ka=(
            "რადისონ ბლუ ივერია თბილისის ცენტრში მდებარე თანამედროვე "
            "და მაღალი კლასის სასტუმროა. სასტუმრო გამოირჩევა თანამედროვე "
            "ინტერიერით, კომფორტული ოთახებით, ქალაქის ულამაზესი ხედებით "
            "და მაღალი დონის მომსახურებით. მისი ცენტრალური მდებარეობა "
            "სტუმრებს საშუალებას აძლევს მარტივად მიაღწიონ თბილისის "
            "მთავარ ღირსშესანიშნაობებს, რესტორნებსა და სავაჭრო უბნებს. "
            "სასტუმრო შესაფერისია როგორც საქმიანი მოგზაურობისთვის, "
            "ასევე დასვენებისა და ტურისტული ვიზიტებისთვის."
        ),

        description_en=(
            "Radisson Blu Iveria Hotel is a modern upscale hotel located "
            "in the heart of Tbilisi. The hotel features contemporary "
            "interiors, comfortable rooms, beautiful city views and "
            "high-quality hospitality. Its central location provides "
            "easy access to Tbilisi's main attractions, restaurants and "
            "shopping areas. The hotel is suitable for both business "
            "travelers and leisure guests."
        ),

        city="Tbilisi",

        featured_image=(
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/"
            "hotel-images/radisson/Gemini_Generated_Image_njcenynjcenynjce.jpg"
        ),

        rating=4.5
    )

    db.add(hotel1)
    db.flush()


    # =========================================================
    # HOTEL 1 IMAGES
    # =========================================================

    hotel1_images = [
        "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_cyfbdocyfbdocyfb.jpg",
        "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_b9l0l6b9l0l6b9l0.jpg",
        "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_y5bbn3y5bbn3y5bb.jpg",
        "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_px1ytpx1ytpx1ytp.jpg"
    ]

    for image_url in hotel1_images:
        db.add(
            HotelImage(
                hotel_id=hotel1.id,
                source=image_url
            )
        )


    # =========================================================
    # HOTEL 1 - SINGLE
    # =========================================================

    add_rooms(
        hotel1.id,
        single_type.id,
        "ერთადგილიანი ოთახი",
        "Single Room",

        "კომფორტული ერთადგილიანი ოთახი განკუთვნილია ერთი "
        "სტუმრისთვის. ოთახში განთავსებულია კომფორტული საწოლი, "
        "სამუშაო მაგიდა, ტელევიზორი, კონდიციონერი, უფასო Wi-Fi "
        "და პირადი აბაზანა.",

        "A comfortable single room designed for one guest. "
        "The room features a comfortable bed, work desk, TV, "
        "air conditioning, free Wi-Fi and a private bathroom.",

        220,
        1,
        5
    )

    add_room_type_images(
        hotel1.id,
        single_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/SINGLE_IMAGE_1.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/SINGLE_IMAGE_2.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/SINGLE_IMAGE_3.jpg"
        ]
    )


    # =========================================================
    # HOTEL 1 - STANDARD
    # =========================================================

    add_rooms(
        hotel1.id,
        standard_type.id,
        "სტანდარტული ოთახი",
        "Standard Room",

        "მყუდრო და თანამედროვე სტანდარტული ოთახი განკუთვნილია "
        "ერთი ან ორი სტუმრისთვის. ოთახში განთავსებულია კომფორტული "
        "ორადგილიანი საწოლი, სამუშაო მაგიდა და დასასვენებელი სივრცე.",

        "A cozy and modern standard room designed for one or two "
        "guests. The room features a comfortable double bed, "
        "work desk and seating area.",

        280,
        2,
        5
    )

    add_room_type_images(
        hotel1.id,
        standard_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_w5mf0nw5mf0nw5mf.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_tdcv6stdcv6stdcv.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2y9o62y9o62y9o62.jpg"
        ]
    )


    # =========================================================
    # HOTEL 1 - DELUXE
    # =========================================================

    add_rooms(
        hotel1.id,
        deluxe_type.id,
        "დელუქს ოთახი",
        "Deluxe Room",

        "ფართო და ელეგანტური დელუქს ოთახი სტუმრებს სთავაზობს "
        "დამატებით სივრცესა და კომფორტს. ოთახში განთავსებულია "
        "დიდი ორადგილიანი საწოლი, დასასვენებელი ზონა, სამუშაო "
        "მაგიდა, ტელევიზორი და მინიბარი.",

        "A spacious and elegant deluxe room offering additional "
        "space and comfort. The room includes a large double bed, "
        "seating area, work desk, TV and minibar.",

        350,
        2,
        4
    )

    add_room_type_images(
        hotel1.id,
        deluxe_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_w5mf0nw5mf0nw5mf.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_tdcv6stdcv6stdcv.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_8ejodn8ejodn8ejo.jpg"
        ]
    )


    # =========================================================
    # HOTEL 1 - FAMILY
    # =========================================================

    add_rooms(
        hotel1.id,
        family_type.id,
        "ოჯახური ოთახი",
        "Family Room",

        "ფართო ოჯახური ნომერი განკუთვნილია ოჯახებისა და მცირე "
        "ჯგუფებისთვის. ოთახში შესაძლებელია ოთხამდე სტუმრის "
        "კომფორტულად განთავსება.",

        "A spacious family room designed for families and small "
        "groups. The room can comfortably accommodate up to four "
        "guests.",

        480,
        4,
        2
    )

    add_room_type_images(
        hotel1.id,
        family_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_w5mf0nw5mf0nw5mf.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2y9o62y9o62y9o62.jpg"
        ]
    )


    # =========================================================
    # HOTEL 1 - SUITE
    # =========================================================

    add_rooms(
        hotel1.id,
        suite_type.id,
        "ლუქსი",
        "Suite",

        "მდიდრული და ფართო ლუქსი შექმნილია სტუმრებისთვის, "
        "რომლებიც განსაკუთრებულ კომფორტსა და პრემიუმ გამოცდილებას "
        "ეძებენ. ნომერი მოიცავს ცალკე საძინებელსა და მისაღებ სივრცეს.",

        "A luxurious and spacious suite designed for guests seeking "
        "maximum comfort and a premium experience. The suite includes "
        "a separate bedroom and living area.",

        650,
        3,
        2
    )

    add_room_type_images(
        hotel1.id,
        suite_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2tum4j2tum4j2tum.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2y9o62y9o62y9o62.jpg"
        ]
    )


    # =========================================================
    # =========================================================
    # HOTEL 2 - ROOMS HOTEL TBILISI
    # =========================================================
    # =========================================================

    hotel2 = Hotel(
        name_ka="რუმს ჰოტელ თბილისი",
        name_en="Rooms Hotel Tbilisi",

        description_ka=(
            "Rooms Hotel Tbilisi არის თანამედროვე დიზაინის სასტუმრო, "
            "რომელიც გამოირჩევა ინდივიდუალური არქიტექტურით, საინტერესო "
            "ინტერიერითა და მყუდრო ატმოსფეროთი."
        ),

        description_en=(
            "Rooms Hotel Tbilisi is a stylish design hotel known for its "
            "distinctive architecture, unique interiors and cozy atmosphere."
        ),

        city="Tbilisi",

        featured_image=(
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/"
            "hotel-images/rooms-hotel/Firefly_Gemini%20Flash.png"
        ),

        rating=4.7
    )

    db.add(hotel2)
    db.flush()


    # =========================================================
    # HOTEL 2 IMAGES
    # =========================================================

    hotel2_images = [
        "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_l04vsol04vsol04v.jpg",
        "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_3vnvx23vnvx23vnv.jpg",
        "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_35msdj35msdj35ms.jpg"
    ]

    for image_url in hotel2_images:
        db.add(
            HotelImage(
                hotel_id=hotel2.id,
                source=image_url
            )
        )


    # =========================================================
    # HOTEL 2 - SINGLE
    # =========================================================

    add_rooms(
        hotel2.id,
        single_type.id,
        "ერთადგილიანი ოთახი",
        "Single Room",

        "მყუდრო ერთადგილიანი ოთახი შექმნილია ერთი სტუმრისთვის. "
        "ნომერში არის კომფორტული საწოლი, სამუშაო სივრცე, "
        "ტელევიზორი, კონდიციონერი, უფასო Wi-Fi და პირადი აბაზანა.",

        "A cozy single room designed for one guest. The room includes "
        "a comfortable bed, workspace, TV, air conditioning, free Wi-Fi "
        "and a private bathroom.",

        210,
        1,
        5
    )

    add_room_type_images(
        hotel2.id,
        single_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_nt406wnt406wnt40.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_ka8syka8syka8syk.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_w1fwqw1fwqw1fwqw.jpg"
        ]
    )


    # =========================================================
    # HOTEL 2 - STANDARD
    # =========================================================

    add_rooms(
        hotel2.id,
        standard_type.id,
        "სტანდარტული ოთახი",
        "Standard Room",

        "თანამედროვე დიზაინის მყუდრო სტანდარტული ოთახი შექმნილია "
        "კომფორტული დასვენებისთვის. ნომერში არის კომფორტული საწოლი, "
        "სამუშაო სივრცე, ტელევიზორი, კონდიციონერი და უფასო Wi-Fi.",

        "A cozy standard room with a contemporary design created for "
        "a comfortable stay. The room features a comfortable bed, "
        "workspace, TV, air conditioning and free Wi-Fi.",

        250,
        2,
        5
    )

    add_room_type_images(
        hotel2.id,
        standard_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_nt406wnt406wnt40.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_ka8syka8syka8syk.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_w1fwqw1fwqw1fwqw.jpg"
        ]
    )


    # =========================================================
    # HOTEL 2 - DELUXE
    # =========================================================

    add_rooms(
        hotel2.id,
        deluxe_type.id,
        "დელუქს ოთახი",
        "Deluxe Room",

        "ფართო დელუქს ოთახი შექმნილია სტუმრებისთვის, რომლებიც "
        "მეტ სივრცესა და კომფორტს ანიჭებენ უპირატესობას. ნომერში "
        "განთავსებულია დიდი საწოლი, დასასვენებელი სივრცე, სამუშაო "
        "მაგიდა, ტელევიზორი და მინიბარი.",

        "A spacious deluxe room designed for guests who prefer "
        "additional space and comfort. The room features a large bed, "
        "seating area, work desk, TV and minibar.",

        390,
        2,
        4
    )

    add_room_type_images(
        hotel2.id,
        deluxe_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_4icwao4icwao4icw.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_3osbsc3osbsc3osb.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_ka8syka8syka8syk.jpg"
        ]
    )


    # =========================================================
    # HOTEL 2 - FAMILY
    # =========================================================

    add_rooms(
        hotel2.id,
        family_type.id,
        "ოჯახური ოთახი",
        "Family Room",

        "ფართო ოჯახური ოთახი განკუთვნილია ოჯახებისა და მცირე "
        "ჯგუფებისთვის. ნომერში შესაძლებელია ოთხამდე სტუმრის "
        "კომფორტულად განთავსება.",

        "A spacious family room designed for families and small groups. "
        "The room can comfortably accommodate up to four guests.",

        450,
        4,
        2
    )

    add_room_type_images(
        hotel2.id,
        family_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_4icwao4icwao4icw.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_3osbsc3osbsc3osb.jpg"
        ]
    )


    # =========================================================
    # HOTEL 2 - SUITE
    # =========================================================

    add_rooms(
        hotel2.id,
        suite_type.id,
        "ლუქსი",
        "Suite",

        "პრემიუმ კლასის ფართო ლუქსი სტუმრებს სთავაზობს "
        "კომფორტულ საძინებელსა და ცალკე მისაღებ სივრცეს.",

        "A premium spacious suite featuring a comfortable bedroom "
        "and separate living area.",

        600,
        3,
        2
    )

    add_room_type_images(
        hotel2.id,
        suite_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_4icwao4icwao4icw.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_3osbsc3osbsc3osb.jpg"
        ]
    )


    # =========================================================
    # =========================================================
    # HOTEL 3 - TBILISI MARRIOTT
    # =========================================================
    # =========================================================

    hotel3 = Hotel(
        name_ka="თბილისი მერიოტი",
        name_en="Tbilisi Marriott Hotel",

        description_ka=(
            "თბილისი მერიოტი ქალაქის ცენტრში მდებარე მაღალი კლასის "
            "სასტუმროა, რომელიც ისტორიულ ელემენტებს თანამედროვე "
            "კომფორტთან აერთიანებს. სასტუმრო სტუმრებს სთავაზობს "
            "ელეგანტურ ოთახებს, მაღალი დონის მომსახურებას და თბილისის "
            "მთავარ ღირსშესანიშნაობებთან მოსახერხებელ მდებარეობას."
        ),

        description_en=(
            "Tbilisi Marriott Hotel is an upscale hotel located in the "
            "city center, combining historic character with modern comfort. "
            "The hotel offers elegant rooms, high-quality service and a "
            "convenient location close to Tbilisi's main attractions."
        ),

        city="Tbilisi",

        featured_image=(
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/"
            "hotel-images/hotel/Gemini_Generated_Image_8nfx9c8nfx9c8nfx.jpg"
        ),

        rating=4.6
    )

    db.add(hotel3)
    db.flush()


    # =========================================================
    # HOTEL 3 IMAGES
    # =========================================================

    hotel3_images = [
        "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/33624c0e-ff7c-4d39-afa7-11306e3d4aba.jpg",
        "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_jkpi1wjkpi1wjkpi.jpg",
        "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_tr6q0htr6q0htr6q.jpg",
        "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_novv9pnovv9pnovv.jpg"
    ]

    for image_url in hotel3_images:
        db.add(
            HotelImage(
                hotel_id=hotel3.id,
                source=image_url
            )
        )


    # =========================================================
    # HOTEL 3 - SINGLE
    # =========================================================

    add_rooms(
        hotel3.id,
        single_type.id,
        "ერთადგილიანი ოთახი",
        "Single Room",

        "ელეგანტური ერთადგილიანი ოთახი განკუთვნილია ერთი "
        "სტუმრისთვის. ნომერი აღჭურვილია კომფორტული საწოლით, "
        "სამუშაო სივრცით, ტელევიზორით, კონდიციონერით, "
        "უფასო Wi-Fi-ით და პირადი აბაზანით.",

        "An elegant single room designed for one guest. "
        "The room features a comfortable bed, workspace, TV, "
        "air conditioning, free Wi-Fi and a private bathroom.",

        240,
        1,
        5
    )

    add_room_type_images(
        hotel3.id,
        single_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_c046kvc046kvc046.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_jj7hbyjj7hbyjj7h.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_novv9pnovv9pnovv.jpg"
        ]
    )


    # =========================================================
    # HOTEL 3 - STANDARD
    # =========================================================

    add_rooms(
        hotel3.id,
        standard_type.id,
        "სტანდარტული ოთახი",
        "Standard Room",

        "ელეგანტური სტანდარტული ოთახი შექმნილია კომფორტული "
        "დასვენებისთვის. ნომერში არის კომფორტული საწოლი, "
        "სამუშაო სივრცე, ტელევიზორი, კონდიციონერი, Wi-Fi "
        "და თანამედროვე პირადი აბაზანა.",

        "An elegant standard room designed for a comfortable stay. "
        "The room includes a comfortable bed, workspace, TV, "
        "air conditioning, Wi-Fi and a modern private bathroom.",

        290,
        2,
        5
    )

    add_room_type_images(
        hotel3.id,
        standard_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_c046kvc046kvc046.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_jj7hbyjj7hbyjj7h.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_novv9pnovv9pnovv.jpg"
        ]
    )


    # =========================================================
    # HOTEL 3 - DELUXE
    # =========================================================

    add_rooms(
        hotel3.id,
        deluxe_type.id,
        "დელუქს ოთახი",
        "Deluxe Room",

        "ელეგანტური და ფართო დელუქს ნომერი უზრუნველყოფს მაღალი "
        "დონის კომფორტს როგორც დასასვენებლად, ასევე საქმიანი "
        "მოგზაურობისთვის.",

        "An elegant and spacious deluxe room providing a high level "
        "of comfort for both leisure and business travelers.",

        420,
        2,
        4
    )

    add_room_type_images(
        hotel3.id,
        deluxe_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_c046kvc046kvc046.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_jj7hbyjj7hbyjj7h.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_novv9pnovv9pnovv.jpg"
        ]
    )


    # =========================================================
    # HOTEL 3 - FAMILY
    # =========================================================

    add_rooms(
        hotel3.id,
        family_type.id,
        "ოჯახური ოთახი",
        "Family Room",

        "ფართო ოჯახური ნომერი შექმნილია ოჯახებისთვის ან მცირე "
        "ჯგუფებისთვის. ოთახში შესაძლებელია ოთხამდე სტუმრის "
        "კომფორტულად განთავსება.",

        "A spacious family room designed for families or small groups. "
        "The room can comfortably accommodate up to four guests.",

        500,
        4,
        2
    )

    add_room_type_images(
        hotel3.id,
        family_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_57y3pc57y3pc57y3.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_ct1z9pct1z9pct1z.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_7i22yh7i22yh7i22.jpg"
        ]
    )


    # =========================================================
    # HOTEL 3 - SUITE
    # =========================================================

    add_rooms(
        hotel3.id,
        suite_type.id,
        "ლუქსი",
        "Suite",

        "მდიდრული ლუქსი შექმნილია სტუმრებისთვის, რომლებიც "
        "პრემიუმ კომფორტს ეძებენ. ნომერი მოიცავს ცალკე საძინებელსა "
        "და მისაღებ სივრცეს.",

        "A luxurious suite designed for guests seeking premium comfort. "
        "The suite includes a separate bedroom and living area.",

        700,
        3,
        2
    )

    add_room_type_images(
        hotel3.id,
        suite_type.id,
        [
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_c046kvc046kvc046.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_jj7hbyjj7hbyjj7h.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_novv9pnovv9pnovv.jpg"
        ]
    )


    # =========================================================
    # COMMIT
    # =========================================================

    db.commit()

    print()
    print("==============================================")
    print("SEED COMPLETED SUCCESSFULLY")
    print("==============================================")
    print("Hotels: 3")
    print("Rooms: 54")
    print("Room types: 5")
    print("Room images: 0")
    print("Room type images: added")
    print("==============================================")


except Exception as e:

    db.rollback()

    print()
    print("==============================================")
    print("ERROR")
    print("==============================================")
    print(e)
    print("==============================================")


finally:

    db.close()