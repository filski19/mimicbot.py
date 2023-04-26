# mimicbot.py
A personal discord bot which can be used to copy and mimics members names and avatars.
This is not a public bot, this is a basic guide on how you could set it up on your own server.
On the discord developer portal create a bot application and give it permission requirements to be able to perform its tasks.
You can then invite the bot to your server, and run the file in this repository.
In the last line of the script, replace bot.run('example) with bot.run('YourPersonalBotToken')
I used command prompt on my personal machine and typed "python3 mimicbot.py" (Note, you must have python 3 installed on your machine and be in the directory of the script)

The command prefix is "!"
The three commands are 
!set_avatar @member
!set_name @member
!join (channel id)

Member being the user in which the bot will copy the name or avatar of.

