from app.database import SessionLocal

from app.models.hotel import Hotel
from app.models.room import Room
from app.models.room_type import RoomType
from app.models.hotel_image import HotelImage
from app.models.room_image import RoomImage


db = SessionLocal()

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

    db.add_all([
        standard_type,
        deluxe_type,
        suite_type,
        family_type
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

        featured_image="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_njcenynjcenynjce.jpg",

        rating=4.5
    )

    db.add(hotel1)
    db.flush()

    # =========================================================
    # HOTEL 1 IMAGES
    # =========================================================

    db.add_all([
        HotelImage(
            hotel_id=hotel1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_cyfbdocyfbdocyfb.jpg"
        ),
        HotelImage(
            hotel_id=hotel1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_b9l0l6b9l0l6b9l0.jpg"
        ),
        HotelImage(
            hotel_id=hotel1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_y5bbn3y5bbn3y5bb.jpg"
        ),
        HotelImage(
            hotel_id=hotel1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_px1ytpx1ytpx1ytp.jpg"
        )
    ])

    # =========================================================
    # HOTEL 1 - STANDARD ROOM
    # =========================================================

    standard_room1 = Room(
        hotel_id=hotel1.id,
        room_type_id=standard_type.id,

        name_ka="სტანდარტული ოთახი",
        name_en="Standard Room",

        description_ka=(
            "მყუდრო და თანამედროვე სტანდარტული ოთახი განკუთვნილია "
            "ერთი ან ორი სტუმრისთვის. ოთახში განთავსებულია კომფორტული "
            "ორადგილიანი საწოლი, სამუშაო მაგიდა და დასასვენებელი სივრცე. "
            "სტუმრებს შეუძლიათ ისარგებლონ უფასო Wi-Fi-ით, ტელევიზორით, "
            "კონდიციონერით და პირადი თანამედროვე აბაზანით. ოთახის "
            "ინტერიერი შექმნილია მშვიდი და კომფორტული დასვენებისთვის."
        ),

        description_en=(
            "A cozy and modern standard room designed for one or two guests. "
            "The room features a comfortable double bed, work desk and "
            "seating area. Guests can enjoy free Wi-Fi, TV, air conditioning "
            "and a modern private bathroom. The interior is designed to "
            "provide a relaxing and comfortable stay."
        ),

        price_per_night=280,
        max_guests=2,
        reservation_count=0
    )

    db.add(standard_room1)
    db.flush()

    db.add_all([
        RoomImage(
            room_id=standard_room1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_w5mf0nw5mf0nw5mf.jpg"
        ),
        RoomImage(
            room_id=standard_room1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_tdcv6stdcv6stdcv.jpg"
        ),
        RoomImage(
            room_id=standard_room1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2y9o62y9o62y9o62.jpg"
        )
    ])

    # =========================================================
    # HOTEL 1 - DELUXE ROOM
    # =========================================================

    deluxe_room1 = Room(
        hotel_id=hotel1.id,
        room_type_id=deluxe_type.id,

        name_ka="დელუქს ოთახი",
        name_en="Deluxe Room",

        description_ka=(
            "ფართო და ელეგანტური დელუქს ოთახი სტუმრებს სთავაზობს "
            "დამატებით სივრცესა და კომფორტს. ოთახში განთავსებულია დიდი "
            "ორადგილიანი საწოლი, დასასვენებელი ზონა, სამუშაო მაგიდა, "
            "ტელევიზორი და მინიბარი. ასევე ხელმისაწვდომია კონდიციონერი, "
            "უფასო Wi-Fi და თანამედროვე პირადი აბაზანა. ოთახის ფანჯრებიდან "
            "სტუმრებს შეუძლიათ დატკბნენ თბილისის ქალაქის ხედებით."
        ),

        description_en=(
            "A spacious and elegant deluxe room offering additional space "
            "and comfort. The room includes a large double bed, seating area, "
            "work desk, TV and minibar. Guests also have access to air "
            "conditioning, free Wi-Fi and a modern private bathroom. "
            "The windows offer beautiful views of Tbilisi."
        ),

        price_per_night=350,
        max_guests=2,
        reservation_count=0
    )

    db.add(deluxe_room1)
    db.flush()

    db.add_all([
        RoomImage(
            room_id=deluxe_room1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_w5mf0nw5mf0nw5mf.jpg"
        ),
        RoomImage(
            room_id=deluxe_room1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_tdcv6stdcv6stdcv.jpg"
        ),
        RoomImage(
            room_id=deluxe_room1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_8ejodn8ejodn8ejo.jpg"
        )
    ])

    # =========================================================
    # HOTEL 1 - SUITE
    # =========================================================

    suite_room1 = Room(
        hotel_id=hotel1.id,
        room_type_id=suite_type.id,

        name_ka="ლუქსი",
        name_en="Suite",

        description_ka=(
            "მდიდრული და ფართო ლუქსი შექმნილია სტუმრებისთვის, რომლებიც "
            "განსაკუთრებულ კომფორტსა და პრემიუმ გამოცდილებას ეძებენ. "
            "ნომერი მოიცავს ცალკე საძინებელსა და მისაღებ სივრცეს, დიდ "
            "საწოლს, კომფორტულ დივანს, სამუშაო მაგიდას და მინიბარს. "
            "სტუმრებს ასევე შეუძლიათ ისარგებლონ დიდი ტელევიზორით, "
            "კონდიციონერით, უფასო Wi-Fi-ით და თანამედროვე აბაზანით. "
            "ოთახი გამოირჩევა ფართო სივრცითა და ქალაქის ხედებით."
        ),

        description_en=(
            "A luxurious and spacious suite designed for guests seeking "
            "maximum comfort and a premium experience. The suite includes "
            "a separate bedroom and living area, a large bed, comfortable "
            "sofa, work desk and minibar. Guests can also enjoy a large TV, "
            "air conditioning, free Wi-Fi and a modern bathroom. "
            "The suite offers generous space and beautiful city views."
        ),

        price_per_night=650,
        max_guests=3,
        reservation_count=0
    )

    db.add(suite_room1)
    db.flush()

    db.add_all([
        RoomImage(
            room_id=suite_room1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2tum4j2tum4j2tum.jpg"
        ),
        RoomImage(
            room_id=suite_room1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2y9o62y9o62y9o62.jpg"
        ),
        RoomImage(
            room_id=suite_room1.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/radisson/Gemini_Generated_Image_2y9o62y9o62y9o62.jpg"
        )
    ])

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
            "ოთახებს, დასასვენებელ სივრცეებსა და მაღალი ხარისხის "
            "მომსახურებას. სასტუმრო კარგი არჩევანია როგორც ტურისტული, "
            "ასევე საქმიანი ვიზიტებისთვის."
        ),

        description_en=(
            "Rooms Hotel Tbilisi is a stylish design hotel known for its "
            "distinctive architecture, unique interiors and cozy atmosphere. "
            "Located in one of Tbilisi's notable neighborhoods, the hotel "
            "offers comfortable rooms, relaxing spaces and high-quality "
            "hospitality. It is a great choice for both leisure and business "
            "travelers."
        ),

        city="Tbilisi",

        featured_image="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Firefly_Gemini%20Flash.png",

        rating=4.7
    )

    db.add(hotel2)
    db.flush()

    # =========================================================
    # HOTEL 2 IMAGES
    # =========================================================

    db.add_all([
        HotelImage(
            hotel_id=hotel2.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_l04vsol04vsol04v.jpg"
        ),
        HotelImage(
            hotel_id=hotel2.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_3vnvx23vnvx23vnv.jpg"
        ),
        HotelImage(
            hotel_id=hotel2.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_35msdj35msdj35ms.jpg"
        )
    ])

    # =========================================================
    # HOTEL 2 - STANDARD ROOM
    # =========================================================

    standard_room2 = Room(
        hotel_id=hotel2.id,
        room_type_id=standard_type.id,

        name_ka="სტანდარტული ოთახი",
        name_en="Standard Room",

        description_ka=(
            "თანამედროვე დიზაინის მყუდრო სტანდარტული ოთახი, რომელიც "
            "შექმნილია კომფორტული დასვენებისთვის. ნომერში არის "
            "კომფორტული საწოლი, სამუშაო სივრცე, ტელევიზორი, "
            "კონდიციონერი, უფასო Wi-Fi და პირადი აბაზანა. ოთახის "
            "ინტერიერი აერთიანებს თანამედროვე დიზაინსა და პრაქტიკულ "
            "სივრცეს, რაც იდეალურია როგორც მოკლე, ასევე ხანგრძლივი "
            "ვიზიტებისთვის."
        ),

        description_en=(
            "A cozy standard room with a contemporary design created for "
            "a comfortable stay. The room features a comfortable bed, "
            "workspace, TV, air conditioning, free Wi-Fi and a private "
            "bathroom. The interior combines modern design with practical "
            "space, making it suitable for both short and extended stays."
        ),

        price_per_night=250,
        max_guests=2,
        reservation_count=0
    )

    db.add(standard_room2)
    db.flush()

    db.add_all([
        RoomImage(
            room_id=standard_room2.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_nt406wnt406wnt40.jpg"
        ),
        RoomImage(
            room_id=standard_room2.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_ka8syka8syka8syk.jpg"
        ),
        RoomImage(
            room_id=standard_room2.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_w1fwqw1fwqw1fwqw.jpg"
        )
    ])

    # =========================================================
    # HOTEL 2 - DELUXE ROOM
    # =========================================================

    deluxe_room2 = Room(
        hotel_id=hotel2.id,
        room_type_id=deluxe_type.id,

        name_ka="დელუქს ოთახი",
        name_en="Deluxe Room",

        description_ka=(
            "ფართო დელუქს ოთახი შექმნილია სტუმრებისთვის, რომლებიც "
            "მეტ სივრცესა და კომფორტს ანიჭებენ უპირატესობას. ნომერში "
            "განთავსებულია დიდი საწოლი, დასასვენებელი სივრცე, სამუშაო "
            "მაგიდა, ტელევიზორი და მინიბარი. ოთახს აქვს თანამედროვე "
            "აბაზანა, კონდიციონერი და უფასო Wi-Fi. თანამედროვე ინტერიერი "
            "ქმნის მშვიდ და სასიამოვნო გარემოს დასვენებისთვის."
        ),

        description_en=(
            "A spacious deluxe room designed for guests who prefer "
            "additional space and comfort. The room features a large bed, "
            "seating area, work desk, TV and minibar. It also includes a "
            "modern bathroom, air conditioning and free Wi-Fi. "
            "The contemporary interior creates a relaxing atmosphere."
        ),

        price_per_night=390,
        max_guests=2,
        reservation_count=0
    )

    db.add(deluxe_room2)
    db.flush()

    db.add_all([
        RoomImage(
            room_id=deluxe_room2.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_4icwao4icwao4icw.jpg"
        ),
        RoomImage(
            room_id=deluxe_room2.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_3osbsc3osbsc3osb.jpg"
        ),
        RoomImage(
            room_id=deluxe_room2.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/rooms-hotel/Gemini_Generated_Image_ka8syka8syka8syk.jpg"
        )
    ])

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
            "მთავარ ღირსშესანიშნაობებთან მოსახერხებელ მდებარეობას. "
            "სასტუმრო შესაფერისია როგორც საქმიანი მოგზაურებისთვის, "
            "ასევე ტურისტებისთვის და ოჯახებისთვის."
        ),

        description_en=(
            "Tbilisi Marriott Hotel is an upscale hotel located in the "
            "city center, combining historic character with modern comfort. "
            "The hotel offers elegant rooms, high-quality service and a "
            "convenient location close to Tbilisi's main attractions. "
            "It is suitable for business travelers, tourists and families."
        ),

        city="Tbilisi",

        featured_image="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_8nfx9c8nfx9c8nfx.jpg",

        rating=4.6
    )

    db.add(hotel3)
    db.flush()

    # =========================================================
    # HOTEL 3 IMAGES
    # =========================================================

    db.add_all([
        HotelImage(
            hotel_id=hotel3.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/33624c0e-ff7c-4d39-afa7-11306e3d4aba.jpg"
        ),
        HotelImage(
            hotel_id=hotel3.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_jkpi1wjkpi1wjkpi.jpg"
        ),
        HotelImage(
            hotel_id=hotel3.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_tr6q0htr6q0htr6q.jpg"
        ),
        HotelImage(
            hotel_id=hotel3.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_novv9pnovv9pnovv.jpg"
        )
    ])

    # =========================================================
    # HOTEL 3 - DELUXE ROOM
    # =========================================================

    deluxe_room3 = Room(
        hotel_id=hotel3.id,
        room_type_id=deluxe_type.id,

        name_ka="დელუქს ოთახი",
        name_en="Deluxe Room",

        description_ka=(
            "ელეგანტური და ფართო დელუქს ნომერი უზრუნველყოფს მაღალი "
            "დონის კომფორტს როგორც დასასვენებლად, ასევე საქმიანი "
            "მოგზაურობისთვის. ოთახში არის დიდი საწოლი, სამუშაო სივრცე, "
            "დასასვენებელი ზონა, ტელევიზორი, მინიბარი, კონდიციონერი, "
            "უფასო Wi-Fi და პირადი თანამედროვე აბაზანა. ოთახის "
            "დიზაინი აერთიანებს კლასიკურ ელემენტებსა და თანამედროვე "
            "კომფორტს."
        ),

        description_en=(
            "An elegant and spacious deluxe room providing a high level "
            "of comfort for both leisure and business travelers. It "
            "includes a large bed, workspace, seating area, TV, minibar, "
            "air conditioning, free Wi-Fi and a modern private bathroom. "
            "The design combines classic elements with modern comfort."
        ),

        price_per_night=420,
        max_guests=2,
        reservation_count=0
    )

    db.add(deluxe_room3)
    db.flush()

    db.add_all([
        RoomImage(
            room_id=deluxe_room3.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_c046kvc046kvc046.jpg"
        ),
        RoomImage(
            room_id=deluxe_room3.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_jj7hbyjj7hbyjj7h.jpg"
        ),
        RoomImage(
            room_id=deluxe_room3.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_novv9pnovv9pnovv.jpg"
        )
    ])

    # =========================================================
    # HOTEL 3 - FAMILY ROOM
    # =========================================================

    family_room3 = Room(
        hotel_id=hotel3.id,
        room_type_id=family_type.id,

        name_ka="ოჯახური ოთახი",
        name_en="Family Room",

        description_ka=(
            "ფართო ოჯახური ნომერი შექმნილია ოჯახებისთვის ან მცირე "
            "ჯგუფებისთვის. ოთახში შესაძლებელია ოთხამდე სტუმრის "
            "კომფორტულად განთავსება. ნომერი მოიცავს კომფორტულ საწოლებს, "
            "დასასვენებელ სივრცეს, სამუშაო მაგიდას, ტელევიზორს, "
            "კონდიციონერს, უფასო Wi-Fi-ს და დიდ თანამედროვე აბაზანას. "
            "ოთახის სივრცე საშუალებას იძლევა ოჯახმა კომფორტულად "
            "გაატაროს როგორც მოკლე, ასევე ხანგრძლივი ვიზიტი."
        ),

        description_en=(
            "A spacious family room designed for families or small groups. "
            "The room can comfortably accommodate up to four guests. "
            "It includes comfortable beds, seating area, work desk, TV, "
            "air conditioning, free Wi-Fi and a large modern bathroom. "
            "The spacious layout makes it suitable for both short and "
            "extended family stays."
        ),

        price_per_night=500,
        max_guests=4,
        reservation_count=0
    )

    db.add(family_room3)
    db.flush()

    db.add_all([
        RoomImage(
            room_id=family_room3.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_57y3pc57y3pc57y3.jpg"
        ),
        RoomImage(
            room_id=family_room3.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_ct1z9pct1z9pct1z.jpg"
        ),
        RoomImage(
            room_id=family_room3.id,
            source="https://jqlclezeahbawibogfxf.supabase.co/storage/v1/object/public/hotel-images/hotel/Gemini_Generated_Image_7i22yh7i22yh7i22.jpg"
        )
    ])

    # =========================================================
    # COMMIT
    # =========================================================

    db.commit()

    print("==============================================")
    print("Hotels, rooms and images successfully added!")
    print("==============================================")


except Exception as e:

    db.rollback()

    print("==============================================")
    print(f"Error: {e}")
    print("==============================================")


finally:

    db.close()