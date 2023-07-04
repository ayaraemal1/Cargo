# Cargo management system

The Cargo management system is a Django-based web application that allows users to manage cargoes, cars, and locations. It provides functionalities to create, update, and delete cargoes, as well as retrieve information about cargoes and cars based on various criteria.

# Features

- Create, update, and delete cargoes with specific characteristics, including pick-up and delivery locations, weight, and description.
- Manage cars current location.
- Define locations with details such as city, state, zip code, latitude, and longitude on the start of te app using csv table.
- Retrieve information about a specific cargo, including its pick-up and delivery locations, weight, description, and a list of all the cars numbers with their distances to the cargo.
- Filter cargoes based on its weight.
- Retrieve a list of cargoes along with the count of nearby cars within a specified distance.

# Installation

1. Clone the repository: `git clone https://github.com/air17/Cargo-management-system.git`
2. Navigate to the project's directory: `cd Cargo-management-system`
3. Copy `.env.template` file to `.env` and fill it in.
4. Start the application using Docker Compose: `docker compose up -d`
5. Access the application through your web browser at http://localhost:8000.

# API Endpoints

- [Postman Documentation](https://documenter.getpostman.com/view/24517363/2s93m7WMiw): Link to the documentation that provides detailed information about the API endpoints and usage.

- [Download Postman Collection](https://raw.githubusercontent.com/air17/Cargo-management-system/master/Cargo_system.postman_collection.json): Link to download the Postman collection file that contains pre-configured requests for the API. This collection can be imported into Postman to quickly explore and test the API endpoints.

- [OpenAPI schema](https://github.com/air17/Cargo-management-system/blob/master/freight_car_locator/openapi-schema.yml)
