# BOILERPLATE APP (FOR DUMMIES)

# CONVENTIONS

## Notice: Please be aware that deviating from the established conventions may result in unforeseen issues for which you will be solely responsible

- use camel case
- for foreing key, use "fk_" before the name of column, like "fk_userId".
- use LF(never CRLF) as default.

Prisma Usage

```shell
  prisma [command]
```

Commands

            init   Set up Prisma for your app
        generate   Generate artifacts (e.g. Prisma Client)
              db   Manage your database schema and lifecycle
         migrate   Migrate your database
          studio   Browse your data with Prisma Studio
        validate   Validate your Prisma schema
          format   Format your Prisma schema
         version   Displays Prisma version info
           debug   Displays Prisma debug info

Flags

     --preview-feature   Run Preview Prisma commands
     --help, -h          Show additional information about a command

Examples

  Set up a new Prisma project

  ```shell
  prisma init
```

  Generate artifacts (e.g. Prisma Client)

  ```shell
  prisma generate
```
  
  Browse your data

  ```shell
  prisma studio
```
  
  Create migrations from your Prisma schema, apply them to the database, generate artifacts (e.g. Prisma Client)

  ```shell
  prisma migrate dev
```
  
  Pull the schema from an existing database, updating the Prisma schema

  ```shell
  prisma db pull 
```

  Push the Prisma schema state to the database

  ```shell
  prisma db push
```
  
## for start database postgresql

  ```shell
  docker compose up -D
```

## commits pattern

<https://www.conventionalcommits.org/en/v1.0.0/>

## Problem Details for HTTP APIs

<https://datatracker.ietf.org/doc/html/rfc7807>

# RELEASES

for publish a release of project, after commit use

```shell
npm run release
```

and follow the steps.

## Conventional Commits micro guide

- `feat`: Addition of a new feature or functionality to the project.
- `fix`: Correction of an existing bug or issue in the code.
- `docs`: Changes to documentation, such as README updates, code comments, or API documentation.
- `style`: Changes that do not affect the code logic, such as formatting, indentation, adding whitespace, or styling changes.
- `refactor`: Refactoring of existing code, without changing functional behavior.
- `test`: Addition or modification of tests, including unit tests, integration tests, or adjustments to test scripts.
- `chore`: Maintenance tasks, configuration adjustments, dependency updates, or any other changes that do not fit into the previous categories.
