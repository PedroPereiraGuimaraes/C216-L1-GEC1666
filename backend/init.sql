CREATE TABLE professores (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  materia VARCHAR(255) NOT NULL,
  data_nascimento VARCHAR(255) NOT NULL
)