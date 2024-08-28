
CREATE TABLE roles (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	description varchar NOT NULL,
	CONSTRAINT roles_pk PRIMARY KEY (id)
);


--===>>> Claims:
CREATE TABLE claims (
	id int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	description varchar NOT NULL,
	active bool NOT NULL DEFAULT true,
	CONSTRAINT claims_pk PRIMARY KEY (id)
);

--===>>> UserClaims:
CREATE TABLE user_claims (
	user_id int8 NOT NULL,
	claim_id int8 NOT NULL,
	CONSTRAINT user_claims_un UNIQUE (user_id, claim_id)
);


--===>>> Users:
CREATE TABLE users (
	id int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	"name" varchar NOT NULL,
	email varchar NOT NULL,
	"password" varchar NOT NULL,
	role_id int4 NOT NULL,
	created_at date NOT NULL,
	updated_at date NULL,
	CONSTRAINT users_pk PRIMARY KEY (id)
);

-- users foreign keys
ALTER TABLE users ADD CONSTRAINT users_fk FOREIGN KEY (role_id) REFERENCES roles(id);


-- user_claims foreign keys
ALTER TABLE user_claims ADD CONSTRAINT user_claims_fk FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE user_claims ADD CONSTRAINT user_claims_fk_1 FOREIGN KEY (claim_id) REFERENCES claims(id);


-- Inserindo dados nas tabelas

INSERT INTO roles (description) VALUES ('Admin');
INSERT INTO roles (description) VALUES ('User');
INSERT INTO roles (description) VALUES ('Guest');


INSERT INTO claims (description, active) VALUES ('Read', true);
INSERT INTO claims (description, active) VALUES ('Write', true);
INSERT INTO claims (description, active) VALUES ('Delete', false);


INSERT INTO users ("name", email, "password", role_id, created_at, updated_at) 
VALUES ('Alice', 'alice@example.com', 'password123', 1, '2024-08-28', NULL);
INSERT INTO users ("name", email, "password", role_id, created_at, updated_at) 
VALUES ('Bob', 'bob@example.com', 'password456', 2, '2024-08-28', NULL);
INSERT INTO users ("name", email, "password", role_id, created_at, updated_at) 
VALUES ('Charlie', 'charlie@example.com', 'password789', 3, '2024-08-28', NULL);


INSERT INTO user_claims (user_id, claim_id) VALUES (1, 1);
INSERT INTO user_claims (user_id, claim_id) VALUES (1, 2);
INSERT INTO user_claims (user_id, claim_id) VALUES (2, 1);
INSERT INTO user_claims (user_id, claim_id) VALUES (3, 3);



select usr.name, usr.email, cl.description as claims, rl.description as role from users usr, claims cl, roles rl, user_claims uc
where usr.id = uc.user_id 
and cl.id = uc.claim_id
and rl.id = usr.role_id;








