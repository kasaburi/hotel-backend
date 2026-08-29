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
            "და კომფორტული სასტუმროა. სასტუმრო გამოირჩევა ქალაქის "
            "ულამაზესი ხედებით, თანამედროვე ინტერიერით, მაღალი დონის "
            "მომსახურებით და მოსახერხებელი მდებარეობით. "
            "სასტუმრო იდეალურია როგორც საქმიანი, ასევე დასასვენებელი "
            "მოგზაურობისთვის."
        ),

        description_en=(
            "Radisson Blu Iveria Hotel is a modern and comfortable hotel "
            "located in the heart of Tbilisi. It offers beautiful city "
            "views, contemporary interiors, high-quality service and a "
            "convenient location. The hotel is ideal for both business "
            "and leisure travelers."
        ),

        city="Tbilisi",
        featured_image="https://example.com/radisson-main.jpg",
        rating=4.5
    )

    db.add(hotel1)
    db.flush()


    # HOTEL 1 IMAGES

    db.add_all([
        HotelImage(
            hotel_id=hotel1.id,
            source="https://example.com/radisson-1.jpg"
        ),
        HotelImage(
            hotel_id=hotel1.id,
            source="https://example.com/radisson-2.jpg"
        ),
        HotelImage(
            hotel_id=hotel1.id,
            source="https://example.com/radisson-3.jpg"
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
            "მყუდრო და თანამედროვე სტანდარტული ოთახი, რომელიც იდეალურია "
            "ერთი ან ორი სტუმრისთვის. ოთახში დაგხვდებათ კომფორტული "
            "ორადგილიანი საწოლი, სამუშაო მაგიდა, ტელევიზორი, "
            "კონდიციონერი, უფასო Wi-Fi და თანამედროვე აბაზანა. "
            "ოთახი შექმნილია მშვიდი და კომფორტული დასვენებისთვის."
        ),

        description_en=(
            "A cozy and modern standard room designed for one or two guests. "
            "The room features a comfortable double bed, work desk, TV, "
            "air conditioning, free Wi-Fi and a modern private bathroom. "
            "It is designed for a relaxing and comfortable stay."
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
            source="https://example.com/radisson-standard-1.jpg"
        ),
        RoomImage(
            room_id=standard_room1.id,
            source="https://example.com/radisson-standard-2.jpg"
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
            "ფართო და ელეგანტური დელუქს ოთახი, რომელიც სტუმრებს "
            "სთავაზობს დამატებით სივრცესა და კომფორტს. ოთახში არის "
            "დიდი ორადგილიანი საწოლი, დასასვენებელი ზონა, სამუშაო მაგიდა, "
            "ტელევიზორი, მინიბარი, კონდიციონერი, უფასო Wi-Fi და "
            "თანამედროვე აბაზანა. ფანჯრებიდან შესაძლებელია თბილისის "
            "ქალაქის ხედით დატკბობა."
        ),

        description_en=(
            "A spacious and elegant deluxe room offering additional space "
            "and comfort. The room includes a large double bed, seating area, "
            "work desk, TV, minibar, air conditioning, free Wi-Fi and a "
            "modern private bathroom. Guests can enjoy beautiful city views."
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
            source="https://example.com/radisson-deluxe-1.jpg"
        ),
        RoomImage(
            room_id=deluxe_room1.id,
            source="https://example.com/radisson-deluxe-2.jpg"
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
            "მაქსიმალურ კომფორტსა და განსაკუთრებულ გამოცდილებას ეძებენ. "
            "ნომერი მოიცავს ცალკე საძინებელსა და მისაღებ სივრცეს, "
            "დიდ საწოლს, კომფორტულ დივანს, სამუშაო მაგიდას, მინიბარს, "
            "დიდ ტელევიზორს, თანამედროვე აბაზანას და ქალაქის ხედებს."
        ),

        description_en=(
            "A luxurious and spacious suite designed for guests seeking "
            "maximum comfort and a premium experience. The suite includes "
            "a separate bedroom and living area, large bed, comfortable sofa, "
            "work desk, minibar, large TV, modern bathroom and city views."
        ),

        price_per_night=650,
        max_guests=3,
        reservation_count=0
    )

    db.add(suite_room1)
    db.flush()


    db.add(
        RoomImage(
            room_id=suite_room1.id,
            source="https://example.com/radisson-suite.jpg"
        )
    )


    # =========================================================
    # HOTEL 2 - ROOMS HOTEL TBILISI
    # =========================================================

    hotel2 = Hotel(
        name_ka="რუმს ჰოტელ თბილისი",
        name_en="Rooms Hotel Tbilisi",

        description_ka=(
            "Rooms Hotel Tbilisi არის თანამედროვე დიზაინის სასტუმრო "
            "თბილისის ერთ-ერთ გამორჩეულ უბანში. სასტუმრო აერთიანებს "
            "მყუდრო გარემოს, თანამედროვე არქიტექტურას, საინტერესო "
            "ინტერიერს და მაღალი ხარისხის მომსახურებას."
        ),

        description_en=(
            "Rooms Hotel Tbilisi is a stylish design hotel located in one "
            "of Tbilisi's distinctive neighborhoods. It combines a cozy "
            "atmosphere, contemporary architecture, unique interiors and "
            "high-quality hospitality."
        ),

        city="Tbilisi",
        featured_image="https://example.com/rooms-main.jpg",
        rating=4.7
    )

    db.add(hotel2)
    db.flush()


    db.add_all([
        HotelImage(
            hotel_id=hotel2.id,
            source="https://example.com/rooms-1.jpg"
        ),
        HotelImage(
            hotel_id=hotel2.id,
            source="https://example.com/rooms-2.jpg"
        )
    ])


    # HOTEL 2 - STANDARD

    standard_room2 = Room(
        hotel_id=hotel2.id,
        room_type_id=standard_type.id,

        name_ka="სტანდარტული ოთახი",
        name_en="Standard Room",

        description_ka=(
            "მყუდრო ოთახი თანამედროვე დიზაინით. ნომერი აღჭურვილია "
            "კომფორტული საწოლით, სამუშაო სივრცით, ტელევიზორით, "
            "კონდიციონერით, უფასო Wi-Fi-ით და პირადი აბაზანით. "
            "იდეალურია მოკლე და ხანგრძლივი ვიზიტებისთვის."
        ),

        description_en=(
            "A cozy room with a contemporary design. It features a "
            "comfortable bed, workspace, TV, air conditioning, free Wi-Fi "
            "and a private bathroom. Ideal for both short and extended stays."
        ),

        price_per_night=250,
        max_guests=2,
        reservation_count=0
    )

    db.add(standard_room2)
    db.flush()


    db.add(
        RoomImage(
            room_id=standard_room2.id,
            source="https://example.com/rooms-standard.jpg"
        )
    )


    # HOTEL 2 - DELUXE

    deluxe_room2 = Room(
        hotel_id=hotel2.id,
        room_type_id=deluxe_type.id,

        name_ka="დელუქს ოთახი",
        name_en="Deluxe Room",

        description_ka=(
            "ფართო დელუქს ოთახი შექმნილია მაქსიმალური კომფორტისთვის. "
            "ნომერს აქვს დიდი საწოლი, დასასვენებელი სივრცე, სამუშაო მაგიდა, "
            "მინიბარი, ტელევიზორი და თანამედროვე აბაზანა."
        ),

        description_en=(
            "A spacious deluxe room designed for maximum comfort. "
            "The room features a large bed, seating area, work desk, "
            "minibar, TV and a modern private bathroom."
        ),

        price_per_night=390,
        max_guests=2,
        reservation_count=0
    )

    db.add(deluxe_room2)
    db.flush()


    db.add(
        RoomImage(
            room_id=deluxe_room2.id,
            source="https://example.com/rooms-deluxe.jpg"
        )
    )


    # =========================================================
    # HOTEL 3 - TBILISI MARRIOTT
    # =========================================================

    hotel3 = Hotel(
        name_ka="თბილისი მერიოტი",
        name_en="Tbilisi Marriott Hotel",

        description_ka=(
            "თბილისი მერიოტი ისტორიული და თანამედროვე ელემენტების "
            "შერწყმით შექმნილი მაღალი კლასის სასტუმროა ქალაქის ცენტრში. "
            "სასტუმრო სტუმრებს სთავაზობს კომფორტულ ოთახებს, მაღალი დონის "
            "მომსახურებას და თბილისის მთავარ ღირსშესანიშნაობებთან "
            "მოსახერხებელ მდებარეობას."
        ),

        description_en=(
            "Tbilisi Marriott Hotel is an upscale hotel in the city center "
            "combining historic character with modern comfort. It offers "
            "comfortable rooms, high-quality service and a convenient "
            "location close to Tbilisi's main attractions."
        ),

        city="Tbilisi",
        featured_image="https://example.com/marriott-main.jpg",
        rating=4.6
    )

    db.add(hotel3)
    db.flush()


    db.add_all([
        HotelImage(
            hotel_id=hotel3.id,
            source="https://example.com/marriott-1.jpg"
        ),
        HotelImage(
            hotel_id=hotel3.id,
            source="https://example.com/marriott-2.jpg"
        ),
        HotelImage(
            hotel_id=hotel3.id,
            source="https://example.com/marriott-3.jpg"
        )
    ])


    # HOTEL 3 - DELUXE

    deluxe_room3 = Room(
        hotel_id=hotel3.id,
        room_type_id=deluxe_type.id,

        name_ka="დელუქს ოთახი",
        name_en="Deluxe Room",

        description_ka=(
            "ელეგანტური და ფართო დელუქს ნომერი, რომელიც უზრუნველყოფს "
            "მაღალი დონის კომფორტს. ოთახში არის დიდი საწოლი, სამუშაო "
            "სივრცე, დასასვენებელი ზონა, ტელევიზორი, მინიბარი, "
            "კონდიციონერი, უფასო Wi-Fi და პირადი აბაზანა."
        ),

        description_en=(
            "An elegant and spacious deluxe room providing a high level "
            "of comfort. It includes a large bed, workspace, seating area, "
            "TV, minibar, air conditioning, free Wi-Fi and private bathroom."
        ),

        price_per_night=420,
        max_guests=2,
        reservation_count=0
    )

    db.add(deluxe_room3)
    db.flush()


    db.add(
        RoomImage(
            room_id=deluxe_room3.id,
            source="https://example.com/marriott-deluxe.jpg"
        )
    )


    # HOTEL 3 - FAMILY

    family_room3 = Room(
        hotel_id=hotel3.id,
        room_type_id=family_type.id,

        name_ka="ოჯახური ოთახი",
        name_en="Family Room",

        description_ka=(
            "ფართო ოჯახური ნომერი შექმნილია ოჯახებისთვის ან მცირე "
            "ჯგუფებისთვის. ოთახში შესაძლებელია ოთხამდე სტუმრის განთავსება. "
            "ნომერი მოიცავს კომფორტულ საწოლებს, დასასვენებელ სივრცეს, "
            "დიდ აბაზანას, ტელევიზორს, კონდიციონერს და უფასო Wi-Fi-ს."
        ),

        description_en=(
            "A spacious family room designed for families or small groups. "
            "The room can accommodate up to four guests and includes "
            "comfortable beds, seating area, large bathroom, TV, "
            "air conditioning and free Wi-Fi."
        ),

        price_per_night=500,
        max_guests=4,
        reservation_count=0
    )

    db.add(family_room3)
    db.flush()


    db.add(
        RoomImage(
            room_id=family_room3.id,
            source="https://example.com/marriott-family.jpg"
        )
    )


    # =========================================================
    # COMMIT
    # =========================================================

    db.commit()

    print("Hotels, rooms and images successfully added!")


except Exception as e:

    db.rollback()

    print(f"Error: {e}")


finally:

    db.close()