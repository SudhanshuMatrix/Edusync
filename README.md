<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
<a href="https://github.com/SudhanshuMatrix/Edusync">
    <img src="static/assets/images/logo.png" alt="Logo" width="160" height="120">
  </a>
  <h3 align="center">School Management System</h3>

  <p align="center">
    A comprehensive software solution for managing academic and administrative activities within educational institutions.
    <br />
    <a href="https://github.com/SudhanshuMatrix/Edusync">View Demo</a>
    ·
    <a href="https://github.com/SudhanshuMatrix/Edusync/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/SudhanshuMatrix/Edusync/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#key-features">Key Features</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The School Management System is designed to streamline and enhance the management of academic and administrative activities within educational institutions. It provides secure and personalized access for students and teachers, enabling efficient handling of attendance, homework, grades, and communication.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Built With
* [![Python][Python-url]][Python]
* [![MySQL][MySQL-url]][MySQL]

<!-- KEY FEATURES -->
## Key Features

1. **Student Login:**
   - Secure login for students to access their personalized dashboards.
   - View class schedules, announcements, and school-related information.

2. **Teacher Login:**
   - Secure login for teachers to access their personalized dashboards.
   - Manage class schedules, student attendance, and assignments.

3. **Attendance System:**
   - Digital recording of student attendance by teachers.
   - Real-time attendance tracking and reporting.
   - Notifications for irregular attendance patterns.

4. **Homework System:**
   - Teachers can assign homework with due dates and detailed instructions.
   - Students can submit homework electronically.
   - Teachers can review and grade homework submissions within the system.

5. **Marks System:**
   - Input and manage student grades for assignments, tests, and exams.
   - Generate report cards and performance analytics.
   - Students and parents can view grades and track academic progress.

6. **Chat System:**
   - Integrated messaging platform for communication between students, teachers, and parents.
   - Supports individual and group chats.
   - Ensures secure and monitored communication to enhance collaboration and support.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- TECHNOLOGIES USED -->
## Technologies Used

- **Frontend:** Python (Tkinter)
- **Backend:** Python, (for server-side logic and application development)
- **Database:** MySQL (for data storage and management)
- **Authentication:** Standard login system (username and password)
- **Real-time Communication:** WebSockets (for chat and real-time features)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- INSTALLATION -->
## Installation

To set up the project locally, follow these steps:

1. Clone the repo
   ```sh
   git clone https://github.com/SudhanshuMatrix/Edusync.git
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Set up the database
   ```sh
   python manage.py migrate
   ```
4. Start the development server
   ```sh
   python manage.py runserver
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## Usage

Use this space to show examples of usage and additional screenshots, code examples, or demos.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Implement Student & Teacher Login
- [ ] Implement Student Dashboard
- [ ] Develop Attendance System
- [ ] Integrate Marks System
- [ ] Enhance Chat System

See the [open issues](https://github.com/SudhanshuMatrix/Edusync/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Your Name - sudhanshureal.cat@gmail.com

Project Link: [https://github.com/SudhanshuMatrix/Edusync](https://github.com/SudhanshuMatrix/Edusync)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

List here the resources, libraries, or tools that you have used or were inspired by.

* [Tkinter](https://tkdocs.com)
* [Aiven Cloud](https://aiven.io)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/SudhanshuMatrix/Edusync.svg?style=for-the-badge
[contributors-url]: https://github.com/SudhanshuMatrix/Edusync/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SudhanshuMatrix/Edusync.svg?style=for-the-badge
[forks-url]: https://github.com/SudhanshuMatrix/Edusync/network/members
[stars-shield]: https://img.shields.io/github/stars/SudhanshuMatrix/Edusync.svg?style=for-the-badge
[stars-url]: https://github.com/SudhanshuMatrix/Edusync/stargazers
[issues-shield]: https://img.shields.io/github/issues/SudhanshuMatrix/Edusync.svg?style=for-the-badge
[issues-url]: https://github.com/SudhanshuMatrix/Edusync/issues
[MySQL-url]: https://img.shields.io/badge/Mysql-white?style=for-the-badge&logo=mysql
[Python-url]: https://img.shields.io/badge/python-white?style=for-the-badge&logo=python 
[Python]: https://www.python.org
[MySQL]: https://www.mysql.com  
