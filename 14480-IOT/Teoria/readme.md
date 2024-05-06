# IOT classes
Content's summary


# 1. Middle Term

## 1.1. Lecture 1 - Introdução a UC

Nothing to take a note because is just an introduction 
   
## 1.2. Lecture 2 - Internet das Coisas

- IOT Definition: occurs when electrical, electronic, or mechanical devices communicate with each other over the Internet. IoT facilitates seamless data exchange, enabling objects to improve performance and make informed decisions autonomously;

- IOT Components: Sensors, Electronics, Connectivity, Cloud based Analytics

- IOT sub-areas: 
    - Smart cities: Mobility and Environment 
    - Smart Homes: Energy Efficiency and Quality of Life
    - Rural Areas: Agriculture and Mobility
    - Industry: Automation
    - Monitoring: Health and Telehealth  

- IOT connectivity: 
    - Wired: fast, secure, reliable
    - Short-Range: Bluethooth, Zigbee
    - Wifi: wireless
    - Gateway: Receive and send data using another connectivity

- IOT Arquitecture example: 
    - Sensors & Raspberry Pi
    - Gateway wi-fi router
    - MQTTs Broker
    - API Engine
    - Cloud Database
    - Web App
    - Desktop App

## 1.3. Lecture 3 - Arquitectures and Technologies
Challenge: In design and system is the absence of a general architecture that can simplify the high-level design

- Architecture
    - IOT World Forum Architecture:
        - Data in Motion
            - L1: Physical devices and controllers
            - L2: Connectivity
            - L3: Edge computing
            - L4: Data accumulation
        - Data at rest
            - L5: Data abtraction
            - L6: Application
            - L7: Collaboration and processes

    - Microsoft Architecture:
        - Things:
            - IOT devices
        - Cloud gateway (IOT hub)
        - Insights:
            - Stream processing
            - Storage
            - UI and reporting tools
        - Actions
            - Business integration

- IOT Technologies
    - Devices
        - Edge devices
        - Sensors and atuators
        - Microcontrolers
    - Cloud
    - Data Centers
    - Servers

## 1.4. Lecture 4 - Interoperability

Definition: The ability of two or more systems or components to exchange information and to use the information that has been exchanged

- Types of Interoperability
    - Amoung devices: Exchange informations between devices, Integration of new devices
    - Network: comunnication between differents network's typologies, routing issues, security, optimization, QoS, mobility
    - Sitatics: sintatic code must be the same amoung systems
    - Semantics: campatibility data model amoung systems, be able for diferents agents or services or applications exchange information
    - Plataform: Be able to exchange information between differents SO or domains

- Standards
    - Open
        - oneM2M
        - W3C Web of Things: Focuses on interoperability of device, syntactics and semantics
        - FIWARE
        - ETSI smatM2M
        - Lightweight M2M (LWM2M)
    
    - Close
        - ISO/IEC 21823-1:2019:  Framework, network connectivity, Semantic interoperability
        - IEEE P1451-99: Interoperability and Security
        - IEEE P1931.1: Interoperability
        - IEEE 1934-2018: Fog Computing

 - Fog Computing: Decentralized computing infrastructure in which data, compute, storage and applications are located somewhere between the data source and the cloud

 - SOA Architecture: To solve syntactic interoperability problems mainly based on Restful APIs

 - Semantic web IOT: To solve semantic interoperability

## 1.5. Lecture 5 - 

# 2. Final Term

## 2.1 Overview
There are two folders:
    Codes: In this folder we can see all notebooks and General_Functions
    Virtual Environments: In this folder wwe have all libraries we need to extract data
    
## 2.2 Surveys
Each Survey have a Id,  which we will need to insert for extract 
    
## 2.3 Connections
The extraction came from Qualtrics API, there area about 8 functions with diferents ways to extract.

## 2.4 Start Code
To start a extraction you will find a file called Start_Example.ipynb and replace your Survey's ID and Days of Extraction
    
# 3. Structure of the Surveys
The extraction will start with 5 files survey_full_data, survey_options, survey_questions, responses_full_data, responses_df