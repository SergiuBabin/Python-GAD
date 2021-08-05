create table category(
    name varchar(255) primary key,
    is_base_expense boolean,
    aliases text
);

create table user_info(
    id integer primary key,
    name varchar(255)
);

create table expense(
    id integer,
    amount integer,
    user_id integer,
    created datetime,
    category text,
    note text,
    FOREIGN KEY(category) REFERENCES category(name),
    FOREIGN KEY(user_id) REFERENCES user_info(id),
    PRIMARY KEY (id, user_id)
);

insert into category (name, is_base_expense, aliases)
values
    ("products", true, "food"),
    ("drink", true, "wather, coffee, beer"),
    ("dinner", true, "canteen, lunch, business-lunch, business lunch, eat"),
    ("cafe", true, "restaurant, rest, mac, mcdonald's, mcduck, kfc, ilpatio, dristor, kebab, shaorma"),
    ("transport", false, "metro, buss, taxi"),
    ("phone", false, "vodafone, orange"),
    ("books", false, "literature, book"),
    ("internet", false, "net, telecom, starnet"),
    ("subscriptions", false, "subs, apple music, appel tv, apple books"),
    ("other", false, ""),
    ("utilities", true, "engie, apa nova, telecom");