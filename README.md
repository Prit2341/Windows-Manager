# Windows Manager



Windows Manager is a utility tool designed to simplify and automate various file management tasks on the Windows operating system. It provides four key functionalities to help users maintain their files and optimize storage space efficiently.

## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Functionalities](#functionalities)
  - [Temp Files Cleaner](#temp-files-cleaner)
  - [Recycle Bin Automated](#recycle-bin-automated)
  - [WhatsApp Files Automated](#whatsapp-files-automated)
  - [Files Manager](#files-manager)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About

Windows Manager is a powerful tool created to enhance the file management experience for Windows users. By automating certain tasks, it streamlines the process of cleaning temporary files, managing the Recycle Bin, organizing WhatsApp files, and managing user files that have not been accessed for a specified duration. When you see the code you will probably thinks it's just a piece of code on how you can use them on your PC<br>
😎😎let me explain!

## Installation

First of all, you Have to install all libraries in your global Environment(What I am talking About you already Know that🤔🤔)
oh Not First We have to clone the repo First my bad 🤦‍♂️🤦‍♂️
Clone the repository: `git clone https://github.com/your-username/windows-manager.git`
```
pip install tempfile # for Temp file
pip install pywin32 # for Recycle Bin
pip install watchdog # for WhatsApp Automation
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

### WhatsApp Files Automated

The WhatsApp Files Automated feature simplifies file organization by automatically directing all WhatsApp media files, regardless of the save location, to a specified folder. This ensures that all WhatsApp-related files are neatly stored in one designated location.

### Files Manager

The Files Manager functionality helps users declutter their file system by automatically relocating files that haven't been accessed for a defined period. This option aids in optimizing storage space while keeping essential files organized.

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