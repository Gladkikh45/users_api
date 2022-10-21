create schema main authorization postgres;

grant all on schema main to postgres;

create table if not exists main.users
(
    id             uuid primary key     default gen_random_uuid(),
    created_at     timestamptz not null default now(),
    display_name   varchar     not null,
    login          varchar     not null,
    hash           text        not null,
    deleted_at     timestamptz
);

-- insert into main.users (display_name, login, hash) values ('Bob', 'bob', 'dp');