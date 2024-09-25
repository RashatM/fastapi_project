CREATE TABLE public.bookings (
	id serial4 NOT NULL,
	room_id int4 NULL,
	user_id int4 NULL,
	date_from date NOT NULL,
	date_to date NOT NULL,
	price int4 NOT NULL,
	total_cost int4 NULL GENERATED ALWAYS AS ((date_to - date_from) * price) STORED,
	total_days int4 NULL GENERATED ALWAYS AS (date_to - date_from) STORED,
	CONSTRAINT bookings_pkey PRIMARY KEY (id),
	CONSTRAINT bookings_room_id_fkey FOREIGN KEY (room_id) REFERENCES public.rooms(id),
	CONSTRAINT bookings_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id)
);

CREATE TABLE public.hotels (
	id serial4 NOT NULL,
	"name" varchar NOT NULL,
	"location" varchar NOT NULL,
	services json NULL,
	rooms_quantity int4 NOT NULL,
	image_id int4 NULL,
	CONSTRAINT hotels_pkey PRIMARY KEY (id)
);

CREATE TABLE public.rooms (
	id serial4 NOT NULL,
	hotel_id int4 NOT NULL,
	"name" varchar NOT NULL,
	description varchar NULL,
	price int4 NOT NULL,
	services json NULL,
	quantity int4 NOT NULL,
	image_id int4 NULL,
	CONSTRAINT rooms_pkey PRIMARY KEY (id),
	CONSTRAINT rooms_hotel_id_fkey FOREIGN KEY (hotel_id) REFERENCES public.hotels(id)
);

CREATE TABLE public.users (
	id serial4 NOT NULL,
	email varchar NOT NULL,
	hashed_password varchar NOT NULL,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);
