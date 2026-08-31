
from app.database import SessionLocal

from app.models.hotel import Hotel
from app.models.room import Room
from app.models.room_type import RoomType
from app.models.hotel_image import HotelImage
from app.models.room_image import RoomImage


db = SessionLocal()


# =========================================================
# HELPER FUNCTION - ADD ROOM
# =========================================================

def add_room(
    hotel_id,
    room_type_id,
    name_ka,
    name_en,
    description_ka,
    description_en,
    price,
    max_guests,
    image_urls,
    quantity=1
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

    # Add images to every created room
    for room in rooms:
        for image_url in image_urls:
            db.add(
                RoomImage(
                    room_id=room.id,
                    source=image_url
                )
            )

    return rooms


try:

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
    # HOTEL 1 - RADISSON BLU IVERIA
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
    # HOTEL 1 - SINGLE ROOMS
    # 5 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel1.id,
        room_type_id=single_type.id,

        name_ka="ერთადგილიანი ოთახი",
        name_en="Single Room",

        description_ka=(
            "კომფორტული ერთადგილიანი ოთახი განკუთვნილია ერთი "
            "სტუმრისთვის. ოთახში განთავსებულია კომფორტული საწოლი, "
            "სამუშაო მაგიდა, ტელევიზორი, კონდიციონერი, უფასო Wi-Fi "
            "და პირადი აბაზანა. ოთახი იდეალურია როგორც საქმიანი, "
            "ასევე მოკლე ტურისტული ვიზიტებისთვის."
        ),

        description_en=(
            "A comfortable single room designed for one guest. "
            "The room features a comfortable bed, work desk, TV, "
            "air conditioning, free Wi-Fi and a private bathroom. "
            "It is ideal for both business and short leisure stays."
        ),

        price=220,
        max_guests=1,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/SINGLE_IMAGE_1.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/SINGLE_IMAGE_2.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/SINGLE_IMAGE_3.jpg"
        ],

        quantity=5
    )


    # =========================================================
    # HOTEL 1 - STANDARD ROOMS
    # 5 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel1.id,
        room_type_id=standard_type.id,

        name_ka="სტანდარტული ოთახი",
        name_en="Standard Room",

        description_ka=(
            "მყუდრო და თანამედროვე სტანდარტული ოთახი განკუთვნილია "
            "ერთი ან ორი სტუმრისთვის. ოთახში განთავსებულია კომფორტული "
            "ორადგილიანი საწოლი, სამუშაო მაგიდა და დასასვენებელი სივრცე. "
            "სტუმრებს შეუძლიათ ისარგებლონ უფასო Wi-Fi-ით, ტელევიზორით, "
            "კონდიციონერით და პირადი თანამედროვე აბაზანით."
        ),

        description_en=(
            "A cozy and modern standard room designed for one or two "
            "guests. The room features a comfortable double bed, work "
            "desk and seating area. Guests can enjoy free Wi-Fi, TV, "
            "air conditioning and a modern private bathroom."
        ),

        price=280,
        max_guests=2,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_w5mf0nw5mf0nw5mf.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_tdcv6stdcv6stdcv.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2y9o62y9o62y9o62.jpg"
        ],

        quantity=5
    )


    # =========================================================
    # HOTEL 1 - DELUXE ROOMS
    # 4 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel1.id,
        room_type_id=deluxe_type.id,

        name_ka="დელუქს ოთახი",
        name_en="Deluxe Room",

        description_ka=(
            "ფართო და ელეგანტური დელუქს ოთახი სტუმრებს სთავაზობს "
            "დამატებით სივრცესა და კომფორტს. ოთახში განთავსებულია "
            "დიდი ორადგილიანი საწოლი, დასასვენებელი ზონა, სამუშაო "
            "მაგიდა, ტელევიზორი და მინიბარი. ასევე ხელმისაწვდომია "
            "კონდიციონერი, უფასო Wi-Fi და თანამედროვე პირადი აბაზანა."
        ),

        description_en=(
            "A spacious and elegant deluxe room offering additional "
            "space and comfort. The room includes a large double bed, "
            "seating area, work desk, TV and minibar. Guests also have "
            "access to air conditioning, free Wi-Fi and a modern "
            "private bathroom."
        ),

        price=350,
        max_guests=2,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_w5mf0nw5mf0nw5mf.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_tdcv6stdcv6stdcv.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_8ejodn8ejodn8ejo.jpg"
        ],

        quantity=4
    )


    # =========================================================
    # HOTEL 1 - FAMILY ROOMS
    # 2 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel1.id,
        room_type_id=family_type.id,

        name_ka="ოჯახური ოთახი",
        name_en="Family Room",

        description_ka=(
            "ფართო ოჯახური ნომერი განკუთვნილია ოჯახებისა და მცირე "
            "ჯგუფებისთვის. ოთახში შესაძლებელია ოთხამდე სტუმრის "
            "კომფორტულად განთავსება. ნომერი მოიცავს კომფორტულ საწოლებს, "
            "დასასვენებელ სივრცეს, სამუშაო მაგიდას, ტელევიზორს, "
            "კონდიციონერს, უფასო Wi-Fi-ს და თანამედროვე აბაზანას."
        ),

        description_en=(
            "A spacious family room designed for families and small "
            "groups. The room can comfortably accommodate up to four "
            "guests and includes comfortable beds, seating area, work "
            "desk, TV, air conditioning, free Wi-Fi and a modern bathroom."
        ),

        price=480,
        max_guests=4,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_w5mf0nw5mf0nw5mf.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2y9o62y9o62y9o62.jpg"
        ],

        quantity=2
    )


    # =========================================================
    # HOTEL 1 - SUITES
    # 2 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel1.id,
        room_type_id=suite_type.id,

        name_ka="ლუქსი",
        name_en="Suite",

        description_ka=(
            "მდიდრული და ფართო ლუქსი შექმნილია სტუმრებისთვის, "
            "რომლებიც განსაკუთრებულ კომფორტსა და პრემიუმ გამოცდილებას "
            "ეძებენ. ნომერი მოიცავს ცალკე საძინებელსა და მისაღებ სივრცეს, "
            "დიდ საწოლს, კომფორტულ დივანს, სამუშაო მაგიდას და მინიბარს."
        ),

        description_en=(
            "A luxurious and spacious suite designed for guests seeking "
            "maximum comfort and a premium experience. The suite includes "
            "a separate bedroom and living area, a large bed, comfortable "
            "sofa, work desk and minibar."
        ),

        price=650,
        max_guests=3,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2tum4j2tum4j2tum.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2y9o62y9o62y9o62.jpg"
        ],

        quantity=2
    )


    # =========================================================
    # HOTEL 2 - ROOMS HOTEL TBILISI
    # =========================================================

    hotel2 = Hotel(
        name_ka="რუმს ჰოტელ თბილისი",
        name_en="Rooms Hotel Tbilisi",

        description_ka=(
            "Rooms Hotel Tbilisi არის თანამედროვე დიზაინის სასტუმრო, "
            "რომელიც გამოირჩევა ინდივიდუალური არქიტექტურით, საინტერესო "
            "ინტერიერითა და მყუდრო ატმოსფეროთი. სასტუმრო მდებარეობს "
            "თბილისის გამორჩეულ უბანში და სტუმრებს სთავაზობს კომფორტულ "
            "ოთახებს, დასასვენებელ სივრცეებსა და მაღალი ხარისხის მომსახურებას."
        ),

        description_en=(
            "Rooms Hotel Tbilisi is a stylish design hotel known for its "
            "distinctive architecture, unique interiors and cozy atmosphere. "
            "The hotel offers comfortable rooms, relaxing spaces and "
            "high-quality hospitality."
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
    # HOTEL 2 - SINGLE ROOMS
    # 5 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel2.id,
        room_type_id=single_type.id,

        name_ka="ერთადგილიანი ოთახი",
        name_en="Single Room",

        description_ka=(
            "მყუდრო ერთადგილიანი ოთახი შექმნილია ერთი სტუმრისთვის. "
            "ნომერში არის კომფორტული საწოლი, სამუშაო სივრცე, "
            "ტელევიზორი, კონდიციონერი, უფასო Wi-Fi და პირადი აბაზანა."
        ),

        description_en=(
            "A cozy single room designed for one guest. The room includes "
            "a comfortable bed, workspace, TV, air conditioning, free Wi-Fi "
            "and a private bathroom."
        ),

        price=210,
        max_guests=1,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_nt406wnt406wnt40.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_ka8syka8syka8syk.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_w1fwqw1fwqw1fwqw.jpg"
        ],

        quantity=5
    )


    # =========================================================
    # HOTEL 2 - STANDARD ROOMS
    # 5 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel2.id,
        room_type_id=standard_type.id,

        name_ka="სტანდარტული ოთახი",
        name_en="Standard Room",

        description_ka=(
            "თანამედროვე დიზაინის მყუდრო სტანდარტული ოთახი შექმნილია "
            "კომფორტული დასვენებისთვის. ნომერში არის კომფორტული საწოლი, "
            "სამუშაო სივრცე, ტელევიზორი, კონდიციონერი, უფასო Wi-Fi "
            "და პირადი აბაზანა."
        ),

        description_en=(
            "A cozy standard room with a contemporary design created for "
            "a comfortable stay. The room features a comfortable bed, "
            "workspace, TV, air conditioning, free Wi-Fi and a private bathroom."
        ),

        price=250,
        max_guests=2,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_nt406wnt406wnt40.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_ka8syka8syka8syk.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_w1fwqw1fwqw1fwqw.jpg"
        ],

        quantity=5
    )


    # =========================================================
    # HOTEL 2 - DELUXE ROOMS
    # 4 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel2.id,
        room_type_id=deluxe_type.id,

        name_ka="დელუქს ოთახი",
        name_en="Deluxe Room",

        description_ka=(
            "ფართო დელუქს ოთახი შექმნილია სტუმრებისთვის, რომლებიც "
            "მეტ სივრცესა და კომფორტს ანიჭებენ უპირატესობას. ნომერში "
            "განთავსებულია დიდი საწოლი, დასასვენებელი სივრცე, სამუშაო "
            "მაგიდა, ტელევიზორი და მინიბარი."
        ),

        description_en=(
            "A spacious deluxe room designed for guests who prefer "
            "additional space and comfort. The room features a large bed, "
            "seating area, work desk, TV and minibar."
        ),

        price=390,
        max_guests=2,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_4icwao4icwao4icw.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_3osbsc3osbsc3osb.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_ka8syka8syka8syk.jpg"
        ],

        quantity=4
    )


    # =========================================================
    # HOTEL 2 - FAMILY ROOMS
    # 2 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel2.id,
        room_type_id=family_type.id,

        name_ka="ოჯახური ოთახი",
        name_en="Family Room",

        description_ka=(
            "ფართო ოჯახური ოთახი განკუთვნილია ოჯახებისა და მცირე "
            "ჯგუფებისთვის. ნომერში შესაძლებელია ოთხამდე სტუმრის "
            "კომფორტულად განთავსება."
        ),

        description_en=(
            "A spacious family room designed for families and small groups. "
            "The room can comfortably accommodate up to four guests."
        ),

        price=450,
        max_guests=4,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_4icwao4icwao4icw.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_3osbsc3osbsc3osb.jpg"
        ],

        quantity=2
    )


    # =========================================================
    # HOTEL 2 - SUITES
    # 2 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel2.id,
        room_type_id=suite_type.id,

        name_ka="ლუქსი",
        name_en="Suite",

        description_ka=(
            "პრემიუმ კლასის ფართო ლუქსი სტუმრებს სთავაზობს "
            "კომფორტულ საძინებელსა და ცალკე მისაღებ სივრცეს. "
            "ნომერი აღჭურვილია დიდი საწოლით, დივნით, სამუშაო სივრცით, "
            "ტელევიზორით, მინიბარითა და თანამედროვე აბაზანით."
        ),

        description_en=(
            "A premium spacious suite featuring a comfortable bedroom "
            "and separate living area. The suite includes a large bed, "
            "sofa, workspace, TV, minibar and modern bathroom."
        ),

        price=600,
        max_guests=3,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_4icwao4icwao4icw.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_3osbsc3osbsc3osb.jpg"
        ],

        quantity=2
    )


    # =========================================================
    # HOTEL 3 - TBILISI MARRIOTT
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
    # HOTEL 3 - SINGLE ROOMS
    # 5 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel3.id,
        room_type_id=single_type.id,

        name_ka="ერთადგილიანი ოთახი",
        name_en="Single Room",

        description_ka=(
            "ელეგანტური ერთადგილიანი ოთახი განკუთვნილია ერთი "
            "სტუმრისთვის. ნომერი აღჭურვილია კომფორტული საწოლით, "
            "სამუშაო სივრცით, ტელევიზორით, კონდიციონერით, "
            "უფასო Wi-Fi-ით და პირადი აბაზანით."
        ),

        description_en=(
            "An elegant single room designed for one guest. "
            "The room features a comfortable bed, workspace, TV, "
            "air conditioning, free Wi-Fi and a private bathroom."
        ),

        price=240,
        max_guests=1,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_c046kvc046kvc046.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_jj7hbyjj7hbyjj7h.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_novv9pnovv9pnovv.jpg"
        ],

        quantity=5
    )


    # =========================================================
    # HOTEL 3 - STANDARD ROOMS
    # 5 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel3.id,
        room_type_id=standard_type.id,

        name_ka="სტანდარტული ოთახი",
        name_en="Standard Room",

        description_ka=(
            "ელეგანტური სტანდარტული ოთახი შექმნილია კომფორტული "
            "დასვენებისთვის. ნომერში არის კომფორტული საწოლი, "
            "სამუშაო სივრცე, ტელევიზორი, კონდიციონერი, Wi-Fi "
            "და თანამედროვე პირადი აბაზანა."
        ),

        description_en=(
            "An elegant standard room designed for a comfortable stay. "
            "The room includes a comfortable bed, workspace, TV, "
            "air conditioning, Wi-Fi and a modern private bathroom."
        ),

        price=290,
        max_guests=2,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_c046kvc046kvc046.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_jj7hbyjj7hbyjj7h.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_novv9pnovv9pnovv.jpg"
        ],

        quantity=5
    )


    # =========================================================
    # HOTEL 3 - DELUXE ROOMS
    # 4 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel3.id,
        room_type_id=deluxe_type.id,

        name_ka="დელუქს ოთახი",
        name_en="Deluxe Room",

        description_ka=(
            "ელეგანტური და ფართო დელუქს ნომერი უზრუნველყოფს მაღალი "
            "დონის კომფორტს როგორც დასასვენებლად, ასევე საქმიანი "
            "მოგზაურობისთვის. ოთახში არის დიდი საწოლი, სამუშაო სივრცე, "
            "დასასვენებელი ზონა, ტელევიზორი, მინიბარი, კონდიციონერი, "
            "უფასო Wi-Fi და პირადი თანამედროვე აბაზანა."
        ),

        description_en=(
            "An elegant and spacious deluxe room providing a high level "
            "of comfort for both leisure and business travelers. It "
            "includes a large bed, workspace, seating area, TV, minibar, "
            "air conditioning, free Wi-Fi and a modern private bathroom."
        ),

        price=420,
        max_guests=2,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_c046kvc046kvc046.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_jj7hbyjj7hbyjj7h.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_novv9pnovv9pnovv.jpg"
        ],

        quantity=4
    )


    # =========================================================
    # HOTEL 3 - FAMILY ROOMS
    # 2 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel3.id,
        room_type_id=family_type.id,

        name_ka="ოჯახური ოთახი",
        name_en="Family Room",

        description_ka=(
            "ფართო ოჯახური ნომერი შექმნილია ოჯახებისთვის ან მცირე "
            "ჯგუფებისთვის. ოთახში შესაძლებელია ოთხამდე სტუმრის "
            "კომფორტულად განთავსება. ნომერი მოიცავს კომფორტულ საწოლებს, "
            "დასასვენებელ სივრცეს, სამუშაო მაგიდას, ტელევიზორს, "
            "კონდიციონერს, უფასო Wi-Fi-ს და დიდ თანამედროვე აბაზანას."
        ),

        description_en=(
            "A spacious family room designed for families or small groups. "
            "The room can comfortably accommodate up to four guests. "
            "It includes comfortable beds, seating area, work desk, TV, "
            "air conditioning, free Wi-Fi and a large modern bathroom."
        ),

        price=500,
        max_guests=4,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_57y3pc57y3pc57y3.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_ct1z9pct1z9pct1z.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_7i22yh7i22yh7i22.jpg"
        ],

        quantity=2
    )


    # =========================================================
    # HOTEL 3 - SUITES
    # 2 ROOMS
    # =========================================================

    add_room(
        hotel_id=hotel3.id,
        room_type_id=suite_type.id,

        name_ka="ლუქსი",
        name_en="Suite",

        description_ka=(
            "მდიდრული ლუქსი შექმნილია სტუმრებისთვის, რომლებიც "
            "პრემიუმ კომფორტს ეძებენ. ნომერი მოიცავს ცალკე საძინებელსა "
            "და მისაღებ სივრცეს, დიდ საწოლს, დივანს, სამუშაო მაგიდას, "
            "ტელევიზორს, მინიბარს და თანამედროვე აბაზანას."
        ),

        description_en=(
            "A luxurious suite designed for guests seeking premium comfort. "
            "The suite includes a separate bedroom and living area, large bed, "
            "sofa, work desk, TV, minibar and modern bathroom."
        ),

        price=700,
        max_guests=3,

        image_urls=[
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_c046kvc046kvc046.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_jj7hbyjj7hbyjj7h.jpg",
            "https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_novv9pnovv9pnovv.jpg"
        ],

        quantity=2
    )


    # =========================================================
    # COMMIT
    # =========================================================

    db.commit()

    print("==============================================")
    print("Hotels, rooms and images successfully added!")
    print("==============================================")
    print("Hotel 1: 18 rooms")
    print("Hotel 2: 18 rooms")
    print("Hotel 3: 18 rooms")
    print("TOTAL: 54 rooms")
    print("==============================================")


except Exception as e:

    db.rollback()

    print("==============================================")
    print(f"Error: {e}")
    print("==============================================")


finally:

    db.close()

