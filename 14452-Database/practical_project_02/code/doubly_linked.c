#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_COLUMNS 109
#define MAX_COLUMN_LENGTH 256  // Increase if you have longer data in any column

typedef struct Node {
    char data[MAX_COLUMNS][MAX_COLUMN_LENGTH];
    struct Node* next;
    struct Node* prev;
} Node;

// Function prototypes
void readCSVAndPopulateList(const char* filename, Node** head, int* nodeCount);
void searchByDestAirportID(Node* head, const char* airportID);

Node* createNode(char data[MAX_COLUMNS][MAX_COLUMN_LENGTH]) {
    // ... (No changes from your provided code)
}

void append(Node** head, char data[MAX_COLUMNS][MAX_COLUMN_LENGTH], int* nodeCount) {
    Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        Node* temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->prev = temp;
    }
    (*nodeCount)++; // Increment the node count
}

void readCSVAndPopulateList(const char* filename, Node** head, int* nodeCount) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    char buffer[10240];  // Increase buffer size if needed
    char row[MAX_COLUMNS][MAX_COLUMN_LENGTH];
    int columnCount = 0;

    fgets(buffer, sizeof(buffer), file); // Read the header line and ignore it

    while (fgets(buffer, sizeof(buffer), file)) {
        char* token = strtok(buffer, ",");
        columnCount = 0;

        while (token != NULL && columnCount < MAX_COLUMNS) {
            strncpy(row[columnCount], token, MAX_COLUMN_LENGTH - 1);
            row[columnCount][MAX_COLUMN_LENGTH - 1] = '\0'; // Ensure null-termination
            token = strtok(NULL, ",");
            columnCount++;
        }

        append(head, row, nodeCount); // Pass node count to append
    }

    fclose(file);
}

can you merge this in my code bellow:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_COLUMNS 109
#define MAX_COLUMN_LENGTH 256  // Increase if you have longer data in any column

typedef struct Node {
    char data[MAX_COLUMNS][MAX_COLUMN_LENGTH];
    struct Node* next;
    struct Node* prev;
} Node;

// Function prototypes
void readCSVAndPopulateList(const char* filename, Node** head);
void searchByDestAirportID(Node* head, const char* airportID);

// Node-related functions
Node* createNode(char data[MAX_COLUMNS][MAX_COLUMN_LENGTH]) {
    // ... (No changes from your provided code)
}

void append(Node** head, char data[MAX_COLUMNS][MAX_COLUMN_LENGTH]) {
    // ... (No changes from your provided code)
}

// Function to read CSV and populate the list
void readCSVAndPopulateList(const char* filename, Node** head) {
    // ... (No changes from your provided code)
}

// Function to search for a node with a specific airport ID in the 'DestAirportID' column
void searchByDestAirportID(Node* head, const char* airportID) {
    Node* current = head;
    int destAirportIDIndex = 21;  // Replace with the actual column index for 'DestAirportID'
    int step = 0;
    bool found = false;

    printf("Searching for flights with DestAirportID: %s\n", airportID);
    while (current != NULL) {
        step++;
        if (strcmp(current->data[destAirportIDIndex], airportID) == 0) {
            found = true;
            printf("Step %d: Flight found with DestAirportID %s\n", step, airportID);
            // Here you can print out the relevant flight information
        }
        current = current->next;
    }

    if (!found) {
        printf("No flights found with DestAirportID %s\n", airportID);
    }
}

int main() {
    Node* head = NULL;
    int nodeCount = 0;  // Initialize node count

    readCSVAndPopulateList("C:\\temp\\b_plus_tree\\On_Time_Reporting_Carrier_On_Time_Performance.csv", &head, &nodeCount);

    printf("Total number of nodes (rows) in the list: %d\n", nodeCount);

    char airportID[MAX_COLUMN_LENGTH];
    printf("Enter the DestAirportID to search for: ");
    scanf("%s", airportID);
    airportID[MAX_COLUMN_LENGTH - 1] = '\0';  // Ensure input is not too long

    searchByDestAirportID(head, airportID);

    // Free the list
    Node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}
