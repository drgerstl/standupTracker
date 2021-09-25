# Who's Left?
 
Who's Left? is a tracking app for stand-ups. For those times when you can't remember who is yet to go. It allows you to keep track a number of items:
- Who is attending
- Who is leading the meeting
- Who has yet to speak
- Who has spoken
- How many people are attending the meeting
 
## Installation
 
Here is how you get started tracking who you can pass it to next.
 
1. Place all of the files in a single folder. 
2. To customize the list of names displayed or to change the GUI settings, edit the constants.py file.
3. Run the standup.py file with Python. 
 
## Usage

Upon running the program, no employees will be selected and all their names will be grayed out. Check the 'Attending' box for those employees in attendance. This will then make their name selectable. If you click on a selectable name, it will add '- HOST' to their name, indicating they are the one leading the meeting. Only one host can be selected at a time. You can click a chosen host again to deselect them, or if you uncheck the 'Attending' box, the host role will be removed. 

Addtionally, when you check that someone is attending, their name will be displayed in red. Once you check the box for 'To present', their name will be displayed in green, indicating that the have spoken, and the 'To present' box will change to 'Done'. This is also able to be toggled. 

At the bottom you can click the 'All Attending' button to have every employee as marked in attendance. Conversely, you 
can click the 'Clear' button to clear all checkboxes as well as the host label.

In the bottom right corner is an attendance counter which displays the number of people marked as attending.

To close the program, simply click the 'X' in the corner of the window or click the 'Exit' button.

The list of employees to be displayed can be changed in the constants.py file. Currently, the window will accomodate up to 16 employees.

## Contributing
 
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
 
## History
 
Version 1.1 (09-03-2021) - Moving constants into its own file and adding README
Version 1.2 (09-24-2021) - Added utility buttons and attendance counter
 
## Credits
 
Lead Developer - Dan Gerstl
 
## License
 
The MIT License (MIT)

Copyright (c) 2021 Dan Gerstl

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.