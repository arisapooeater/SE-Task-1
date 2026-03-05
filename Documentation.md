# MLP: Character Guide Application (Development Process)
Arisa Komatsu
## Requirements Definition
### Objective
To enable users to search for and sort characters in the animated series 'My Little Pony' by either gender or kind, providing general information on character traits like their alias, residence, occupation etc. This application aims to make MLP lore and information more readily available for the fandom without the need of constant web surfing.

### Functional Requirements
- **Data handling:** System should be able to pull data from API and return it based on user commands.
- **User interaction:** System should allow users to search for characters by name, type or gender and create a personal collection of favourite characters.
- **Error processing:** System should be able to identify invalid inputs and respond with accurate and specific error messages.

### Non-Functional Requirements
- **Performance:**
- **Usability:** System should be structured and clearly accessible for all users. The README file should also provide extensive assistance on using and navigating the project.
- **Reliability:** The API chosen for this project should contain accurate, reliable data on the My Little Pony Universe. Additionally, the system should be able to relay this data without faults. 
- **Security:** API key should be hidden to prevent data theft and unauthorised access.

Non-functional requirements define the quality attributes or constraints of the system. These requirements address aspects such as performance, usability, reliability, and security, which affect how the system performs its functions. These will be defined in more detail in the Determining Specifications Phase.

Example
The book reservation process should complete within 2 seconds of the user submitting a reservation request.

The system must be available 99.9% of the time, ensuring high reliability and uptime.

User data and reservation details must be encrypted to ensure security and privacy.

The feature should be accessible and usable on both desktop and mobile devices, adhering to responsive design principles.\

### Constraints
- 
Constraints are the limitations or restrictions that must be considered during the development of the feature. These could be technical, legal, regulatory, or organisational constraints.

Example
The feature must integrate with the existing library management system without requiring significant changes to the database schema.

The solution must comply with data protection regulations (e.g., GDPR, CCPA) concerning user data storage and handling.

The feature should be implemented using the existing technology stack (e.g., Django for the backend, React for the frontend).

The project budget is limited, so the solution should be cost-effective without requiring additional third-party licenses or services.

### Acceptance Criteria
- Users can successfully search for a character and receive accurate information within 2 seconds.
- Users can successfully choose to sort all characters into different categories (eg. sex, type) and receive accurate information within 2 seconds.
- The system prevents users from adding characters that are already inside the user's collection.

## Determining Specification
### Functional Specifications
### Non-Functional Specifications
**Wording of messages:** 

Overall tone of system messages and menu should be very friendly and catering to the user and must maintain a warm character while giving clear and readable responses. 

**Main Menu:** 

Main menu should be both well structured and aesthetically pleasing with small embellishments to lean into the fantasy genre of My Little Pony. The menu options should be cleary visible, and easy to select. Users should be able to select their option easily with an understanding of what the option does and what results they should expect.

**Frames:** 

System messages and menus should be enclosed in a box with visual structure, whereas user input fields should have a line above and below for emphasis.

**Timing:**

 All system actions (eg. loading main menu, printing search results etc.) should occur within 2-3 seconds and navigating the project should feel natural and streamlined to users.

**Clearing screen:**

 After the system completes a user action, it should ask the user if they are done to clear the screen and reload the main menu for further actions and prevent a cluttered and confusing interface.

## Design
### Structure Chart
### Flowchart
### Pseudocode
### Data Dictionary
### Gantt Chart
## Development
## Integration
## Testing and Debugging
### Student Feedback #1 - Yuna Shin
- feedback based on functional and nonfunctional requirements, response time, load testing and the suitability of the requirements.txt and README.md file

### Student Feedback #2 - Isabella Usacheva
- feedback based on functional and nonfunctional requirements, response time, load testing and the suitability of the requirements.txt and README.md file

## Maintenance
Evaluate the role that maintenance would play in the continued implementation of this software 