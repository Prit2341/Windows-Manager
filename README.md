# Windows Manager



Windows Manager is a utility tool designed to simplify and automate various file management tasks on the Windows operating system. It provides six key functionalities to help users maintain their files and optimize storage space efficiently and become more productive.

## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Functionalities](#functionalities)
  - [Temp Files Cleaner](#temp-files-cleaner)
  - [Recycle Bin Automated](#recycle-bin-automated)
  - [Auto Sleep the Windows](#auto-sleep-the-windows)
  - [Files Manager](#files-manager)
  - [PDF Summrizer](#pdf-summrizer)
  - [PDF to DOCX](#pdf-to-docx)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About

Windows Manager is a powerful tool created to enhance the file management experience for Windows users. By automating certain tasks, it streamlines the process of cleaning temporary files, managing the Recycle Bin, organizing WhatsApp files, PDF Summrizer, PDF to DOCX and managing user files that have not been accessed for a specified duration. When you see the code you will probably thinks it's just a piece of code on how you can use them on your PC<br>
😎😎let me explain!

## Installation

Before diving in, ensure you've installed all the necessary libraries in your virtual environment (as you're probably already aware). Now, let's start by cloning the repository.<br>
Clone the repository:
```
https://github.com/Prit2341/Windows-Manager.git
```
Then Install  <strong>Requirement.txt<strong> file in your virtual enviroment
```
pip install -r requirements.txt
```
Now for the Windows Setup file
## Python Script Scheduling

#### Scheduled Task

Use the Windows Task Scheduler to run your Python script at specific intervals. You can schedule it to run once every few minutes, hours, or even on specific days.

#### Infinite Loop

You can create an infinite loop in your Python script using a ```while True``` loop. However, running an infinite loop is not recommended for long-term processes, as it can consume system resources continuously.

#### Windows Service

For more complex and long-running tasks, you can create a Windows Service using a library like ```pywin32```. Windows Services are designed to run continuously in the background.

#### Run as a Background Process

You can run your Python script in the background by launching it from the command prompt with the ```pythonw``` command instead of ```python```. The ```pythonw``` command prevents the Python script from opening a console window and runs it silently in the background.

Here's how you can use the Scheduled Task method:

1. Open the Windows Task Scheduler ```(taskschd.msc)``` from the Start menu.

2. Click on "Create Basic Task" from the Actions pane on the right.

3. Follow the wizard to set up the task. Choose the frequency and interval you want the task to run.

4. In the "Action" step, select "Start a program" and browse to select your Python executable (usually ```python.exe```) and provide the full path to your Python script.

5. Complete the wizard and save the scheduled task.

Now, your Python script will be scheduled to run at the specified intervals.

## Functionalities

### Temp Files Cleaner

The Temp Files Cleaner functionality allows users to remove unnecessary temporary files from their system, freeing up valuable disk space. Running this feature periodically is recommended to maintain system performance.

### Recycle Bin Automated

With Recycle Bin Automation, users no longer need to worry about emptying their Recycle Bin manually. This functionality automatically clears the Recycle Bin at specified intervals, ensuring a clutter-free system.

### Auto Sleep the Windows

Optimize energy usage and system performance with automated sleep mode activation. Enjoy enhanced energy efficiency without compromising accessibility, thanks to intelligent sleep mode activation during periods of inactivity.

### Files Manager

The Files Manager functionality helps users declutter their file system by automatically relocating files that haven't been accessed for a defined period. This option aids in optimizing storage space while keeping essential files organized.

### PDF Summrizer

Extract key insights efficiently from PDF documents, saving you valuable time. Whether it's research papers or lengthy reports, our summarizer intelligently condenses content, allowing you to focus on what matters most.

### PDF to DOCX

Seamlessly convert PDF files to editable DOCX format for enhanced versatility. Unlock the potential of your documents by effortlessly editing, formatting, and collaborating on them using familiar tools like Microsoft Word.

## Contributing

Thank you for considering contributing to Windows Manager! I welcome any contributions that improve the functionality, performance, or user experience of this tool.

### Contributing Guidelines

Before you start contributing, please take a moment to review the following guidelines:

- **Bug Reports**: If you find any issues or bugs while using Windows Manager, please [submit a detailed bug report](https://github.com/Prit2341/Windows-Manager/issues) on this repo's issue tracker.

- **Feature Requests**: Have a feature in mind that would enhance Windows Manager? Feel free to [open a feature request](https://github.com/Prit2341/Windows-Manager/issues) on this repo's issue tracker. Provide a clear and concise description of the proposed feature and its potential benefits.

- **Pull Requests**: To contribute code, you can submit a pull request. Please ensure that you provide a clear explanation of the changes.
## License

Windows Manager is licensed under the MIT License.

You are free to use, modify, distribute, and sublicense the software as long as you include the original copyright notice and disclaimer in all copies or substantial portions of the software.
## Contact

For any questions, feedback, or support regarding Windows Manager, feel free to reach out to me:

- Email: [pritmayani359@gmail.com](mailto:pritmayani359@gmail.com)
- LinkedIn: [Prit Mayani]([https://www.linkedin.com/in/yourusername/](https://www.linkedin.com/in/prit-mayani-a35b371b9/))

I'm excited to hear your thoughts and suggestions! Let's make Windows Manager even better together.