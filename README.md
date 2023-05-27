# Cargo-management-system

The Cargo Management App is a Django-based web application that allows users to manage cargos, cars, and locations. It provides functionalities to create, update, and delete cargos, as well as retrieve information about cargos and cars based on various criteria.

# Features

Create, update, and delete cargos with specific characteristics, including pick-up and delivery locations, weight, and description.
Manage cars current location.
Define locations with details such as city, state, zip code, latitude, and longitude on the start of te app using csv table.
Retrieve information about a specific cargo, including its pick-up and delivery locations, weight, description, and a list of all the cars numbers with their distances to the cargo.
Filter and sort cargos based on weight and proximity to cars.
Retrieve a list of cargos along with the count of nearby cars within a specified distance.

# Installation

1. Clone the repository: `git clone https://github.com/air17/Cargo-management-system.git`
2. Navigate to the project's directory: `cd Cargo-management-system`
3. Rename `.env.template` file to `.env` and fill it in.
4. Run `docker compose up -d`
5. It's available at http://localhost:8000
