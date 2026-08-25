0:0:3.816 --> 0:0:13.776
Neville, Ryan L MAJ USARMY AI2C (USA)
I want to read from the file and all of the contents I'm going to name file. Okay, so that object is created, that file object.
0:0:14.776 --> 0:0:31.896
Neville, Ryan L MAJ USARMY AI2C (USA)
To extract each line from that file object, I'm going to do this file.readLines method, and I'm going to store that in this variable lines. That will then give me a list of all of the lines in my file.
0:0:33.96 --> 0:0:37.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, if lines is a list, how can we iterate through it?
0:0:41.16 --> 0:0:42.696
Neville, Ryan L MAJ USARMY AI2C (USA)
If lines is a list.
0:0:43.816 --> 0:0:45.16
Neville, Ryan L MAJ USARMY AI2C (USA)
How can we iterate through it?
0:0:46.216 --> 0:0:55.176
Neville, Ryan L MAJ USARMY AI2C (USA)
with a for loop, right? So we can say for line and lines printed out. So this is just going to print out each line of our input file.
0:0:56.696 --> 0:1:17.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, I'll step through that again because it's your first time seeing it. We're going to use the keyword with open. That opens a context manager. The first argument that goes into that open function is the file that we want to open. Okay, it's a string. In this case, it has to be in the same directory that your Python program is in.
0:1:18.376 --> 0:1:24.56
Neville, Ryan L MAJ USARMY AI2C (USA)
You could give it an absolute path, or you could give it a relative path, OK?
0:1:25.96 --> 0:1:35.496
Neville, Ryan L MAJ USARMY AI2C (USA)
The second argument that goes into that function is either read R, write W, or append A.
0:1:37.616 --> 0:1:41.736
Neville, Ryan L MAJ USARMY AI2C (USA)
What is the difference between reading and writing? Pretty simple question.
0:1:44.296 --> 0:1:50.616
Neville, Ryan L MAJ USARMY AI2C (USA)
One reads the other writes. Yeah, one reads the other writes. Good. Okay, simple, right? What about, what's the difference between writing and appending?
0:1:52.16 --> 0:2:10.456
Neville, Ryan L MAJ USARMY AI2C (USA)
So writing overwrites, I assume. That's right. So if this argument is a W, it's going to overwrite whatever is in this file, starting from the beginning. If it is an A for append, it will add lines to the end. It will not overwrite.
0:2:11.336 --> 0:2:11.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Good.
0:2:14.56 --> 0:2:21.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Delete, and then, and then overwrite, or if you're overwriting the shorter statement onto a longer statement, we'll just overwrite that first couple of lines.
0:2:23.176 --> 0:2:24.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Good question.
0:2:26.696 --> 0:2:41.416
Neville, Ryan L MAJ USARMY AI2C (USA)
I think it will completely rewrite, I think, but check me on that. So you're saying if you have a file that's 100 lines long and we're only writing a 10 line file, is it going to overwrite all 100 lines? Check me on that. I think it will completely rewrite the file.
0:2:43.96 --> 0:2:43.576
Neville, Ryan L MAJ USARMY AI2C (USA)
OK.
0:2:44.936 --> 0:2:45.736
Neville, Ryan L MAJ USARMY AI2C (USA)
Notice.
0:2:46.816 --> 0:3:9.16
Neville, Ryan L MAJ USARMY AI2C (USA)
So we're creating this file object. And this file object then has different methods where we can read what the object has in it. In this case, read lines is what we're showing here, but there's other methods. This creates a list of all of the lines in the file. And then we could go through each line and manipulate them or change them or whatever we want to do.
0:3:9.256 --> 0:3:10.456
Neville, Ryan L MAJ USARMY AI2C (USA)
In this case, we're just printing it out.
0:3:11.576 --> 0:3:11.896
Neville, Ryan L MAJ USARMY AI2C (USA)
OK.
0:3:13.496 --> 0:3:16.856
Neville, Ryan L MAJ USARMY AI2C (USA)
This next block of code is simply just a string.
0:3:17.936 --> 0:3:25.896
Neville, Ryan L MAJ USARMY AI2C (USA)
Excuse me, a list of strings with new line characters at the end, and we're writing that into this output file.
0:3:27.336 --> 0:3:34.136
Neville, Ryan L MAJ USARMY AI2C (USA)
So we're opening the output file, we're opening it in write mode. Again, we're creating a file object.
0:3:36.56 --> 0:3:39.96
Neville, Ryan L MAJ USARMY AI2C (USA)
For each line in this list.
0:3:40.256 --> 0:3:41.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Write it into the file.
0:3:43.656 --> 0:3:47.976
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, file.write the text, which the text is just each line in that list.
0:3:49.136 --> 0:3:49.736
Neville, Ryan L MAJ USARMY AI2C (USA)
Make sense?
0:3:51.216 --> 0:3:53.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Fish. It's the first time we've seen this.
0:3:56.856 --> 0:3:57.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Yes.
0:4:0.136 --> 0:4:12.376
Neville, Ryan L MAJ USARMY AI2C (USA)
two state backslashes or to read it as new box going to the bottom? No, just one, just one back slash N. The back slash N will be just a new line character, yeah. Yep, and it's inside that string.
0:4:13.456 --> 0:4:22.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Good question. Yeah, so this file.write function, it does not automatically put you on a new line, right? We had to add those new line characters in.
0:4:22.976 --> 0:4:34.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, we could do that with the for loop as well, right? We could use the for loop and add in the new line characters and then write. We could do that programmatically instead of changing each line ourselves.
0:4:36.696 --> 0:4:53.576
Neville, Ryan L MAJ USARMY AI2C (USA)
Here's some common actions you can do. This is just so you guys understand that with open statement that opens the context manager, we can read the entire file as a string. We can read line by lines into a list. Okay, we can iterate through.
0:4:54.856 --> 0:4:56.296
Neville, Ryan L MAJ USARMY AI2C (USA)
the file line by line.
0:4:57.576 --> 0:5:0.56
Neville, Ryan L MAJ USARMY AI2C (USA)
These are all open operation or reading operations.
0:5:1.256 --> 0:5:10.936
Neville, Ryan L MAJ USARMY AI2C (USA)
Here's our write operations and here's our append operation. Okay. Is it a preference as far as like now seeing more single quotations versus double?
0:5:12.536 --> 0:5:17.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Whatever you want to do. I usually do double quotes, but that's just a preference. Yeah.
0:5:20.16 --> 0:5:41.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Good question. So there's an older way of doing this. The older way was you would create some sort of file handler, assign it to an open file object, and then you would close that file handler on the back end. This is like a bad practice because that if you forget to close that file handler,
0:5:41.736 --> 0:6:0.296
Neville, Ryan L MAJ USARMY AI2C (USA)
you have this background process running on your machine, and it can slow down your machine, and it can actually cause your computer to crash over time. It'll just accumulate memory. So the correct way to do this is with this with keyword. This will handle the context manager, the opening and closing by yourself.
0:6:0.696 --> 0:6:6.856
Neville, Ryan L MAJ USARMY AI2C (USA)
This is like an older way of doing it. You might see this sometime, but this is kind of like the best practice. Okay.
0:6:10.616 --> 0:6:19.976
Neville, Ryan L MAJ USARMY AI2C (USA)
You can do both in the same line. Okay, I can open one file as input, and I can open another file as output.
0:6:21.56 --> 0:6:26.216
Neville, Ryan L MAJ USARMY AI2C (USA)
And then I can write and read kind of in the same block if I wanted.
0:6:28.496 --> 0:6:34.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Does that make sense? We have two different file objects there. One is called input, one is called output.
0:6:35.736 --> 0:6:39.976
Neville, Ryan L MAJ USARMY AI2C (USA)
And now we can do stuff to both. We can read from one right to the other, whatever.
0:6:41.176 --> 0:6:55.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Is this a true way of basically creating an API in air quotes between two different files? Yeah, you could do like an extract, transform, load, kind of like data pipeline here, where we're the code base.
0:7:1.376 --> 0:7:9.576
Neville, Ryan L MAJ USARMY AI2C (USA)
Yep, exactly, exactly. Yep. Yeah, it's a really good way to manipulate some data, transform it however you need to, and then write it somewhere else.
0:7:12.296 --> 0:7:12.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Ben.
0:7:16.216 --> 0:7:17.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Ohh.
0:7:17.736 --> 0:7:19.96
Neville, Ryan L MAJ USARMY AI2C (USA)
In this case...
0:7:20.536 --> 0:7:25.256
Neville, Ryan L MAJ USARMY AI2C (USA)
I think you can just iterate through the file object as well.
0:7:28.576 --> 0:7:29.736
Neville, Ryan L MAJ USARMY AI2C (USA)
We go back here.
0:7:31.336 --> 0:7:43.176
Neville, Ryan L MAJ USARMY AI2C (USA)
We can do this for line in F. We can loop through the file line by line as well. I'm not sure the difference between this and this, to be honest. I think they both work.
0:7:45.656 --> 0:7:47.176
Neville, Ryan L MAJ USARMY AI2C (USA)
Let's practice this real quick.
0:7:48.456 --> 0:8:10.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Let's first write a Python script that will write 100 random integers ranging from 50 to 100 into a file. Each integer should be on a separate line. So that's task one. Task 2, write another Python script that reads from that file, then finds the minimum value, maximum value, and average.
0:8:10.536 --> 0:8:12.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Of the 100 random integers.
0:8:13.256 --> 0:8:17.976
Neville, Ryan L MAJ USARMY AI2C (USA)
Don't use the min and max functions. Find a way to get these values without a built-in function.
0:8:18.936 --> 0:8:22.616
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, so two scripts are going to write here. One is going to generate a file.
0:8:23.656 --> 0:8:26.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Separate script is going to read from that file and do something with it.
0:8:27.56 --> 0:8:27.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:8:30.856 --> 0:8:32.856
Neville, Ryan L MAJ USARMY AI2C (USA)
I will, yeah, Chris.
0:8:34.96 --> 0:8:34.456
Neville, Ryan L MAJ USARMY AI2C (USA)
Thanks.
0:8:35.896 --> 0:8:36.136
Neville, Ryan L MAJ USARMY AI2C (USA)
So.
0:8:37.376 --> 0:8:38.816
Neville, Ryan L MAJ USARMY AI2C (USA)
What you just previously are.
0:8:39.896 --> 0:8:41.96
Neville, Ryan L MAJ USARMY AI2C (USA)
They might be at the end of the...
0:8:42.216 --> 0:8:44.856
Neville, Ryan L MAJ USARMY AI2C (USA)
No, no, sync your sync your thing. I pushed it this morning.
0:8:50.536 --> 0:8:51.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Sync your repo.
0:8:52.696 --> 0:8:53.576
Neville, Ryan L MAJ USARMY AI2C (USA)
Sink your thing.
0:9:2.456 --> 0:9:2.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:9:4.736 --> 0:9:5.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Yep, yep.
0:9:7.896 --> 0:9:11.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Um, it should those those slides should be at the beginning. I moved them to the beginning as well.
0:9:19.416 --> 0:9:25.816
Neville, Ryan L MAJ USARMY AI2C (USA)
You can talk to your neighbors as well. Like if you need some help, hey, I'm stuck, whatever. Talk to your neighbors about how they might do this.
0:9:28.136 --> 0:9:32.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Kind of work through it on your own as well. We'll take about 10 minutes to work through this.
0:9:33.496 --> 0:9:34.376
Neville, Ryan L MAJ USARMY AI2C (USA)
I'm in a.
0:9:35.496 --> 0:9:39.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Move some of this stuff around so you can see all on one screen. Hold on one second.
0:10:10.536 --> 0:10:11.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Right, there's...
0:10:12.696 --> 0:10:14.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Some things all on one slide there for you.
0:10:21.496 --> 0:10:35.16
Neville, Ryan L MAJ USARMY AI2C (USA)
What's interesting, when you're writing a file, it doesn't have to be created initially. The Python script will create this file. So if output.txt does not exist in your local directory, when you run the script, it'll actually create that file.
0:10:36.96 --> 0:10:37.96
Neville, Ryan L MAJ USARMY AI2C (USA)
Does that make sense?
0:10:38.936 --> 0:10:47.256
Neville, Ryan L MAJ USARMY AI2C (USA)
It'll go, in this case, it'll go in the same directory that we're working in. So wherever that Python script is that you're running, it'll just create this in that same directory.
0:10:49.656 --> 0:10:57.16
Neville, Ryan L MAJ USARMY AI2C (USA)
If you wanted to point it to like an absolute directory, you could, or a relative directory, you could use like the dot dot slash, however you want to do it.
0:11:28.936 --> 0:11:30.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Call an office though.
0:11:54.376 --> 0:11:54.856
Neville, Ryan L MAJ USARMY AI2C (USA)
OK.
0:11:58.776 --> 0:11:59.416
Neville, Ryan L MAJ USARMY AI2C (USA)
To.
0:13:54.376 --> 0:13:55.176
Neville, Ryan L MAJ USARMY AI2C (USA)
There's no check.
0:14:19.816 --> 0:14:20.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Totally.
0:14:40.136 --> 0:14:40.216
Neville, Ryan L MAJ USARMY AI2C (USA)
The.
0:14:45.736 --> 0:14:45.976
Neville, Ryan L MAJ USARMY AI2C (USA)
Oh.
0:15:4.616 --> 0:15:5.96
Neville, Ryan L MAJ USARMY AI2C (USA)
Stop.
0:15:6.696 --> 0:15:8.296
Neville, Ryan L MAJ USARMY AI2C (USA)
That's so beautiful.
0:15:12.376 --> 0:15:15.896
Neville, Ryan L MAJ USARMY AI2C (USA)
But, listening.
0:15:18.136 --> 0:15:18.456
Neville, Ryan L MAJ USARMY AI2C (USA)
****.
0:15:29.656 --> 0:15:29.816
Neville, Ryan L MAJ USARMY AI2C (USA)
What?
0:15:32.56 --> 0:15:32.656
Neville, Ryan L MAJ USARMY AI2C (USA)
I don't get that.
0:15:36.856 --> 0:15:37.896
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, we gonna take that.
0:15:43.496 --> 0:15:43.936
Neville, Ryan L MAJ USARMY AI2C (USA)
See.
0:15:52.776 --> 0:15:53.976
Neville, Ryan L MAJ USARMY AI2C (USA)
What else?
0:15:59.176 --> 0:15:59.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:16:2.136 --> 0:16:2.736
Neville, Ryan L MAJ USARMY AI2C (USA)
Computer.
0:16:9.496 --> 0:16:9.616
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:16:11.496 --> 0:16:14.296
Neville, Ryan L MAJ USARMY AI2C (USA)
I am just a victim.
0:16:22.536 --> 0:16:25.176
Neville, Ryan L MAJ USARMY AI2C (USA)
That's it.
0:16:27.296 --> 0:16:28.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Thank you.
0:16:33.576 --> 0:16:34.136
Neville, Ryan L MAJ USARMY AI2C (USA)
What?
0:16:35.416 --> 0:16:35.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:16:39.976 --> 0:16:40.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Exactly.
0:16:45.416 --> 0:16:46.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Thank you.
0:16:47.736 --> 0:16:50.296
Neville, Ryan L MAJ USARMY AI2C (USA)
I have, that's another one.
0:16:53.656 --> 0:16:53.816
Neville, Ryan L MAJ USARMY AI2C (USA)
And...
0:16:55.416 --> 0:16:55.976
Neville, Ryan L MAJ USARMY AI2C (USA)
Sure.
0:17:0.136 --> 0:17:1.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Normally, and...
0:17:11.16 --> 0:17:12.776
Neville, Ryan L MAJ USARMY AI2C (USA)
I think it is.
0:17:18.296 --> 0:17:18.616
Neville, Ryan L MAJ USARMY AI2C (USA)
Thanks.
0:17:22.496 --> 0:17:22.616
Neville, Ryan L MAJ USARMY AI2C (USA)
So.
0:17:27.536 --> 0:17:27.736
Neville, Ryan L MAJ USARMY AI2C (USA)
Really?
0:17:28.616 --> 0:17:34.856
Neville, Ryan L MAJ USARMY AI2C (USA)
But, so, starting next year, this will be with three of those next year.
0:17:36.616 --> 0:17:37.896
Neville, Ryan L MAJ USARMY AI2C (USA)
It's so fast.
0:17:38.856 --> 0:17:39.936
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, send it.
0:17:41.136 --> 0:17:42.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Thank you.
0:17:46.176 --> 0:17:46.936
Neville, Ryan L MAJ USARMY AI2C (USA)
That's true.
0:17:50.376 --> 0:17:50.456
Neville, Ryan L MAJ USARMY AI2C (USA)
The.
0:17:52.256 --> 0:17:52.856
Neville, Ryan L MAJ USARMY AI2C (USA)
So, I think.
0:17:55.816 --> 0:17:56.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:17:59.416 --> 0:17:59.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:18:1.216 --> 0:18:1.496
Neville, Ryan L MAJ USARMY AI2C (USA)
There.
0:18:6.176 --> 0:18:6.456
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:18:9.816 --> 0:18:11.176
Neville, Ryan L MAJ USARMY AI2C (USA)
I know.
0:18:14.936 --> 0:18:16.56
Neville, Ryan L MAJ USARMY AI2C (USA)
This could.
0:18:17.936 --> 0:18:18.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:18:19.176 --> 0:18:19.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Japan.
0:18:41.656 --> 0:18:42.376
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:18:48.296 --> 0:18:49.576
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:18:50.576 --> 0:18:51.96
Neville, Ryan L MAJ USARMY AI2C (USA)
A couple.
0:18:53.256 --> 0:18:53.696
Neville, Ryan L MAJ USARMY AI2C (USA)
Will you?
0:18:55.576 --> 0:18:55.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:18:59.976 --> 0:19:1.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Completely.
0:19:4.136 --> 0:19:4.456
Neville, Ryan L MAJ USARMY AI2C (USA)
It.
0:19:9.376 --> 0:19:23.976
Neville, Ryan L MAJ USARMY AI2C (USA)
Sorry, as far as.
0:19:27.336 --> 0:19:32.376
Neville, Ryan L MAJ USARMY AI2C (USA)
We wanted to collect.
0:19:33.976 --> 0:19:34.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:19:39.576 --> 0:19:39.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:19:44.696 --> 0:19:44.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:19:46.96 --> 0:19:46.376
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:19:47.416 --> 0:19:47.976
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:19:52.536 --> 0:19:53.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Play it.
0:19:56.976 --> 0:19:57.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Hello.
0:20:1.976 --> 0:20:2.616
Neville, Ryan L MAJ USARMY AI2C (USA)
Six.
0:20:6.336 --> 0:20:6.696
Neville, Ryan L MAJ USARMY AI2C (USA)
Yes.
0:20:10.616 --> 0:20:10.856
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:20:13.376 --> 0:20:13.616
Neville, Ryan L MAJ USARMY AI2C (USA)
Thank you.
0:20:17.136 --> 0:20:17.496
Neville, Ryan L MAJ USARMY AI2C (USA)
And.
0:20:22.696 --> 0:20:23.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Ohh.
0:20:25.976 --> 0:20:26.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:20:27.336 --> 0:20:27.936
Neville, Ryan L MAJ USARMY AI2C (USA)
That's sweet.
0:20:39.416 --> 0:20:39.536
Neville, Ryan L MAJ USARMY AI2C (USA)
And.
0:20:41.816 --> 0:20:41.976
Neville, Ryan L MAJ USARMY AI2C (USA)
Ohh.
0:20:45.96 --> 0:20:45.176
Neville, Ryan L MAJ USARMY AI2C (USA)
Are.
0:20:50.696 --> 0:20:51.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, sure.
0:20:52.776 --> 0:20:53.536
Neville, Ryan L MAJ USARMY AI2C (USA)
It sounds like.
0:20:55.16 --> 0:20:55.176
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:20:56.376 --> 0:20:56.496
Neville, Ryan L MAJ USARMY AI2C (USA)
It.
0:21:1.576 --> 0:21:1.736
Neville, Ryan L MAJ USARMY AI2C (USA)
And.
0:21:4.936 --> 0:21:6.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Thanks.
0:21:10.856 --> 0:21:11.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Bing.
0:21:13.736 --> 0:21:13.856
Neville, Ryan L MAJ USARMY AI2C (USA)
Hot.
0:21:16.16 --> 0:21:16.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:21:18.696 --> 0:21:19.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Xbox.
0:21:22.296 --> 0:21:22.576
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:21:25.376 --> 0:21:26.376
Neville, Ryan L MAJ USARMY AI2C (USA)
That's too good.
0:21:30.56 --> 0:21:30.296
Neville, Ryan L MAJ USARMY AI2C (USA)
One.
0:21:41.576 --> 0:21:42.696
Neville, Ryan L MAJ USARMY AI2C (USA)
I know.
0:21:44.176 --> 0:21:44.456
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:21:46.616 --> 0:21:46.856
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:21:48.216 --> 0:21:59.936
Neville, Ryan L MAJ USARMY AI2C (USA)
So, so, you're trying to read a model first, and remember, you're saying?
0:22:3.176 --> 0:22:7.96
Neville, Ryan L MAJ USARMY AI2C (USA)
So, I, you want to like, so it's.
0:22:12.136 --> 0:22:14.296
Neville, Ryan L MAJ USARMY AI2C (USA)
That's what we've done then.
0:22:16.136 --> 0:22:17.176
Neville, Ryan L MAJ USARMY AI2C (USA)
But.
0:22:20.336 --> 0:22:20.856
Neville, Ryan L MAJ USARMY AI2C (USA)
And her.
0:22:30.416 --> 0:22:31.456
Neville, Ryan L MAJ USARMY AI2C (USA)
Stop.
0:22:36.56 --> 0:22:47.256
Neville, Ryan L MAJ USARMY AI2C (USA)
So, so this is gonna sort this.
0:22:53.336 --> 0:22:53.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Right.
0:22:55.216 --> 0:23:0.96
Neville, Ryan L MAJ USARMY AI2C (USA)
I'm just going to all the people that you write, August 1st.
0:23:1.216 --> 0:23:7.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Beat a file, and then you open that file, right?
0:23:10.696 --> 0:23:11.336
Neville, Ryan L MAJ USARMY AI2C (USA)
So.
0:23:13.696 --> 0:23:14.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Thank you.
0:23:16.136 --> 0:23:16.936
Neville, Ryan L MAJ USARMY AI2C (USA)
It is.
0:23:22.176 --> 0:23:22.456
Neville, Ryan L MAJ USARMY AI2C (USA)
What?
0:23:28.936 --> 0:23:29.896
Neville, Ryan L MAJ USARMY AI2C (USA)
And where should they get?
0:23:31.56 --> 0:23:31.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Just fine.
0:23:33.776 --> 0:23:33.896
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:23:37.976 --> 0:23:42.136
Neville, Ryan L MAJ USARMY AI2C (USA)
And then also.
0:23:49.16 --> 0:23:58.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Do you prefer doing truss balls with complete strangers, or perhaps take the fun up and cry?
0:24:6.56 --> 0:24:6.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:24:9.816 --> 0:24:17.176
Neville, Ryan L MAJ USARMY AI2C (USA)
There is, we should be able to do one of those.
0:24:34.696 --> 0:24:36.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Open over.
0:24:40.776 --> 0:24:41.56
Neville, Ryan L MAJ USARMY AI2C (USA)
No.
0:24:43.656 --> 0:24:44.216
Neville, Ryan L MAJ USARMY AI2C (USA)
All right.
0:24:49.656 --> 0:24:49.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:24:52.56 --> 0:24:52.896
Neville, Ryan L MAJ USARMY AI2C (USA)
Fantastic.
0:24:55.416 --> 0:24:58.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Because we're doing something different.
0:25:1.96 --> 0:25:1.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:25:2.616 --> 0:25:2.736
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:25:11.176 --> 0:25:13.816
Neville, Ryan L MAJ USARMY AI2C (USA)
I'm seeing one.
0:25:16.456 --> 0:25:17.96
Neville, Ryan L MAJ USARMY AI2C (USA)
Thanks.
0:25:23.656 --> 0:25:23.976
Neville, Ryan L MAJ USARMY AI2C (USA)
Yes.
0:25:34.456 --> 0:25:34.616
Neville, Ryan L MAJ USARMY AI2C (USA)
So.
0:25:36.376 --> 0:25:36.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:25:37.816 --> 0:25:38.696
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, thank you.
0:25:40.376 --> 0:25:41.96
Neville, Ryan L MAJ USARMY AI2C (USA)
It's.
0:25:43.816 --> 0:25:44.56
Neville, Ryan L MAJ USARMY AI2C (USA)
OK.
0:25:45.336 --> 0:25:51.336
Neville, Ryan L MAJ USARMY AI2C (USA)
It's all I have to do.
0:25:57.256 --> 0:25:57.576
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:26:0.536 --> 0:26:1.96
Neville, Ryan L MAJ USARMY AI2C (USA)
****.
0:26:6.696 --> 0:26:6.776
Neville, Ryan L MAJ USARMY AI2C (USA)
The.
0:26:8.896 --> 0:26:9.16
Neville, Ryan L MAJ USARMY AI2C (USA)
It.
0:26:11.976 --> 0:26:15.256
Neville, Ryan L MAJ USARMY AI2C (USA)
This is.
0:26:18.856 --> 0:26:19.96
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:26:20.56 --> 0:26:20.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Of.
0:26:23.976 --> 0:26:24.56
Neville, Ryan L MAJ USARMY AI2C (USA)
The.
0:26:37.576 --> 0:26:42.856
Neville, Ryan L MAJ USARMY AI2C (USA)
All right, so if you haven't figured out how to write...
0:26:44.296 --> 0:26:47.576
Neville, Ryan L MAJ USARMY AI2C (USA)
Random numbers to hold on, let me pause my music here.
0:26:49.616 --> 0:26:54.136
Neville, Ryan L MAJ USARMY AI2C (USA)
If you haven't figured out how to write random numbers to a file, let me walk you through this real quick.
0:26:55.136 --> 0:26:56.496
Neville, Ryan L MAJ USARMY AI2C (USA)
I'm going to import random.
0:26:58.216 --> 0:27:10.456
Neville, Ryan L MAJ USARMY AI2C (USA)
I'm going to open a context manager for this file right here. File doesn't exist yet. I just named it file.txt. I'm writing to that file and I'm naming the file object just file. Okay.
0:27:12.376 --> 0:27:25.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Now I want to iterate through this 100 times. I want to do this next block of code 100 times. So I'm just going to arbitrarily write for line range 100. That's going to create a for loop that will execute 100 times.
0:27:26.336 --> 0:27:27.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, create a random number.
0:27:29.256 --> 0:27:37.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Assign it the values 50 to 100. Remember that those are both inclusive because of that.randint method. And then we're writing.
0:27:39.256 --> 0:27:49.736
Neville, Ryan L MAJ USARMY AI2C (USA)
a random number as a string plus a new line character to each line. We're doing that 100 times. So if you watch over here, I'm going to delete this file.
0:27:51.96 --> 0:27:52.136
Neville, Ryan L MAJ USARMY AI2C (USA)
That I've already made.
0:27:54.416 --> 0:27:55.896
Neville, Ryan L MAJ USARMY AI2C (USA)
Now, when I run this...
0:27:57.816 --> 0:28:0.296
Neville, Ryan L MAJ USARMY AI2C (USA)
You'll see over here that file will populate.
0:28:1.696 --> 0:28:13.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Right there, right? And now I can see that it worked, right? Got random numbers here between 50 and 100. I'm just going to play around with this for a second. If I take out this new line character,
0:28:15.336 --> 0:28:16.376
Neville, Ryan L MAJ USARMY AI2C (USA)
And I rerun it.
0:28:20.296 --> 0:28:25.176
Neville, Ryan L MAJ USARMY AI2C (USA)
Well, notice I get a bunch of random numbers, but on top of each other, right?
0:28:27.176 --> 0:28:41.96
Neville, Ryan L MAJ USARMY AI2C (USA)
There's no new line character added when I do this.write method. I could also just add like a space, right? And then I rerun it, which overwrites the current file. Now I have numbers that are separated by a space, right?
0:28:42.616 --> 0:28:51.336
Neville, Ryan L MAJ USARMY AI2C (USA)
But what I really want is I just want a new line character between each of those random numbers, and that's going to make it easier to read and manipulate for the next part.
0:28:52.416 --> 0:28:58.56
Neville, Ryan L MAJ USARMY AI2C (USA)
So I run that again. That's going to overwrite this. Now we have this nice file with 100.
0:28:59.416 --> 0:29:0.456
Neville, Ryan L MAJ USARMY AI2C (USA)
Lines.
0:29:1.536 --> 0:29:2.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Of random numbers.
0:29:3.696 --> 0:29:16.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, I'll leave this up here for you to look at. Try to figure out the second part where you're opening that file, you're reading from it, and then you're trying to discover max, min, and average.
0:29:17.336 --> 0:29:17.576
Neville, Ryan L MAJ USARMY AI2C (USA)
Oh.
0:29:23.656 --> 0:29:28.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, I'll write that on here just so you know. The next question is...
0:29:29.16 --> 0:29:40.456
Neville, Ryan L MAJ USARMY AI2C (USA)
Open this file, find max, min, and average. Do that without using any built-in functions. Okay, meaning like don't use the min, max.
0:29:41.536 --> 0:29:44.696
Neville, Ryan L MAJ USARMY AI2C (USA)
function. Don't even use the length function. You can avoid it.
0:30:58.856 --> 0:30:59.416
Neville, Ryan L MAJ USARMY AI2C (USA)
So, no.
0:31:14.856 --> 0:31:14.936
Neville, Ryan L MAJ USARMY AI2C (USA)
We.
0:31:32.176 --> 0:31:32.376
Neville, Ryan L MAJ USARMY AI2C (USA)
Stop.
0:32:7.96 --> 0:32:21.656
Neville, Ryan L MAJ USARMY AI2C (USA)
So before I even start trying to figure out the max and min and all that stuff, what I would want to do is make sure that I can actually read the file correctly, right? I'm going to do this two ways. I'll print.
0:32:23.656 --> 0:32:33.816
Neville, Ryan L MAJ USARMY AI2C (USA)
this lines list to make sure that works. And then I'll also print each line individually, right, just to make sure that my code is doing what I think it should do.
0:32:40.936 --> 0:32:42.136
Neville, Ryan L MAJ USARMY AI2C (USA)
So, notice.
0:32:43.16 --> 0:32:46.696
Neville, Ryan L MAJ USARMY AI2C (USA)
As I've read this in, what's happened here to my file?
0:32:49.96 --> 0:32:53.336
Neville, Ryan L MAJ USARMY AI2C (USA)
It's adding a new line character for every line, right? And actually we can see that.
0:32:54.416 --> 0:32:55.896
Neville, Ryan L MAJ USARMY AI2C (USA)
Here, as well.
0:32:57.96 --> 0:32:57.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Right.
0:32:59.16 --> 0:33:3.336
Neville, Ryan L MAJ USARMY AI2C (USA)
So there's a way to get rid of that. Does anybody know?
0:33:5.176 --> 0:33:5.976
Neville, Ryan L MAJ USARMY AI2C (USA)
There's a method.
0:33:8.376 --> 0:33:12.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Strip, we can replace it as well with nothing, just replace it, or we can do strip.strip.
0:33:15.56 --> 0:33:15.576
Neville, Ryan L MAJ USARMY AI2C (USA)
What's that?
0:33:17.496 --> 0:33:23.656
Neville, Ryan L MAJ USARMY AI2C (USA)
We can do find left and right. Strip is both sides. It will strip all white space from both sides.
0:33:25.416 --> 0:33:32.376
Neville, Ryan L MAJ USARMY AI2C (USA)
Oh, a list object has no attribute strip. I want to strip each line.
0:33:42.776 --> 0:33:43.256
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:34:30.256 --> 0:34:31.896
Neville, Ryan L MAJ USARMY AI2C (USA)
Are you familiar with this, Luke?
0:34:34.96 --> 0:34:34.696
Neville, Ryan L MAJ USARMY AI2C (USA)
What's that?
0:34:35.896 --> 0:34:36.616
Neville, Ryan L MAJ USARMY AI2C (USA)
A little bit.
0:34:38.856 --> 0:34:39.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Do you know what that's called?
0:34:41.736 --> 0:35:0.736
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, it's a list comprehension. It's, we're not going to teach you it, but it's useful. Basically, I'll show this is like a good example of when to use it. I can take a list, I can iterate through that list, I can apply some sort of transformation.
0:35:0.856 --> 0:35:3.16
Neville, Ryan L MAJ USARMY AI2C (USA)
and I can throw it right back into another list.
0:35:4.816 --> 0:35:6.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, it's called a list comprehension.
0:35:8.376 --> 0:35:14.296
Neville, Ryan L MAJ USARMY AI2C (USA)
I'm going to comment it out and I'll do this the other way, but that's there for you to look at.
0:36:26.456 --> 0:36:26.496
Neville, Ryan L MAJ USARMY AI2C (USA)
I.
0:37:47.576 --> 0:37:55.416
Neville, Ryan L MAJ USARMY AI2C (USA)
I've got my solution for the second part of this problem up here. I'll walk you through it in a few minutes. Keep working on your own.
0:37:57.176 --> 0:37:59.816
Neville, Ryan L MAJ USARMY AI2C (USA)
And I'll talk through how I solved it, just a way.
0:38:18.456 --> 0:38:18.536
Neville, Ryan L MAJ USARMY AI2C (USA)
The.
0:38:34.976 --> 0:38:35.56
Neville, Ryan L MAJ USARMY AI2C (USA)
The.
0:38:52.216 --> 0:38:57.216
Neville, Ryan L MAJ USARMY AI2C (USA)
So I'm running this and I'm getting different answers each time. I'm getting a different min.
0:38:59.256 --> 0:39:4.376
Neville, Ryan L MAJ USARMY AI2C (USA)
Max changes, min and max change. Sometimes my average is changing. Why is that happening? That's really weird.
0:39:9.976 --> 0:39:25.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, Ruben's right. I'm also running this top part where I'm regenerating the random numbers, right? Because they're random, we're going to get a distribution that's not always the same. So the average is going to change. And in some cases, the min and the max are going to change too, right?
0:39:28.296 --> 0:39:33.416
Neville, Ryan L MAJ USARMY AI2C (USA)
So if I commented out this part up here, I'd get the same answer every time.
0:39:35.456 --> 0:39:37.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Right, because we're not regenerating.
0:39:38.376 --> 0:39:40.936
Neville, Ryan L MAJ USARMY AI2C (USA)
See how that's always the same? But now...
0:39:41.816 --> 0:39:43.176
Neville, Ryan L MAJ USARMY AI2C (USA)
By uncomment that.
0:39:44.856 --> 0:39:46.136
Neville, Ryan L MAJ USARMY AI2C (USA)
I'm going to get a different answer.
0:39:48.776 --> 0:39:49.816
Neville, Ryan L MAJ USARMY AI2C (USA)
I save the file.
0:39:52.456 --> 0:39:53.176
Neville, Ryan L MAJ USARMY AI2C (USA)
There we go.
0:40:0.736 --> 0:40:10.456
Neville, Ryan L MAJ USARMY AI2C (USA)
All right, so here's how I solved this. I initialized 4 variables at the beginning of my, I guess when I opened the context manager, I initialized count.
0:40:11.616 --> 0:40:14.376
Neville, Ryan L MAJ USARMY AI2C (USA)
which I'm going to use to track how many lines there are.
0:40:16.216 --> 0:40:19.736
Neville, Ryan L MAJ USARMY AI2C (USA)
I initialize some minimum arbitrarily high.
0:40:20.896 --> 0:40:24.376
Neville, Ryan L MAJ USARMY AI2C (USA)
some maximum that's arbitrarily low. Why did I do that?
0:40:29.976 --> 0:40:40.856
Neville, Ryan L MAJ USARMY AI2C (USA)
So when I create a comparison, if I say if the current number is greater than the max, then that's the new max, right? So if my max is really low.
0:40:42.216 --> 0:40:44.56
Neville, Ryan L MAJ USARMY AI2C (USA)
This has to occur, right?
0:40:45.176 --> 0:41:0.696
Neville, Ryan L MAJ USARMY AI2C (USA)
If I said something like my max is initialized at 100, that may or may not be true, right? So to force this to be true, especially initially, I just made this arbitrarily low. Same thing in the inverse for the minimum. Does that make sense? It's kind of like a hack way to do this, but it works.
0:41:2.296 --> 0:41:4.936
Neville, Ryan L MAJ USARMY AI2C (USA)
And it works because I know the values in my list.
0:41:6.16 --> 0:41:11.736
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, I'm counting how many values there are with the count variable. I'm summing them up each time.
0:41:12.656 --> 0:41:16.376
Neville, Ryan L MAJ USARMY AI2C (USA)
And then, at the end, I'm dividing my sum by my count to get my average.
0:41:17.576 --> 0:41:22.776
Neville, Ryan L MAJ USARMY AI2C (USA)
after I've exited the for loop, right, after I've gone through this 100 times.
0:41:23.696 --> 0:41:24.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Does that make sense?
0:41:31.176 --> 0:41:36.936
Neville, Ryan L MAJ USARMY AI2C (USA)
At the same time? No, I don't think so. No. Yeah, good question.
0:41:40.696 --> 0:41:42.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Just one other minutes to work on this.
0:41:43.416 --> 0:41:45.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Just let me know too, alright?
0:41:46.96 --> 0:41:58.216
Neville, Ryan L MAJ USARMY AI2C (USA)
For those of you that are done, take a 10 minute break. We'll pick up again at noon, okay? We're going to cruise through the next part of class pretty quickly. This is kind of like the main point I wanted to teach you.
0:42:6.216 --> 0:42:6.616
Neville, Ryan L MAJ USARMY AI2C (USA)
H.
0:42:11.96 --> 0:42:11.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Just.
0:42:12.536 --> 0:42:13.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Two.
0:42:21.896 --> 0:42:23.976
Neville, Ryan L MAJ USARMY AI2C (USA)
So, Ryan, you got a question? What's that?
0:42:25.656 --> 0:42:27.416
Neville, Ryan L MAJ USARMY AI2C (USA)
For help? Yes.
0:42:30.56 --> 0:42:30.656
Neville, Ryan L MAJ USARMY AI2C (USA)
And.
0:42:34.536 --> 0:42:34.696
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:42:37.576 --> 0:42:37.976
Neville, Ryan L MAJ USARMY AI2C (USA)
Stay.
0:42:43.736 --> 0:42:48.376
Neville, Ryan L MAJ USARMY AI2C (USA)
So, it is creating.
0:42:51.656 --> 0:42:53.736
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, no, but...
0:42:56.16 --> 0:42:56.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:43:2.656 --> 0:43:6.536
Neville, Ryan L MAJ USARMY AI2C (USA)
What's with that? Sure, I mean, how does it?
0:43:10.376 --> 0:43:11.616
Neville, Ryan L MAJ USARMY AI2C (USA)
Save it.
0:43:15.896 --> 0:43:17.96
Neville, Ryan L MAJ USARMY AI2C (USA)
It's just.
0:43:27.16 --> 0:43:35.96
Neville, Ryan L MAJ USARMY AI2C (USA)
This is being.
0:43:37.336 --> 0:43:38.936
Neville, Ryan L MAJ USARMY AI2C (USA)
Looks like a ticket there.
0:43:40.296 --> 0:43:50.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Just, yeah, so based on where you ran on those loops.
0:43:53.176 --> 0:44:3.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, I wish they would. So, if we wanted to remove anything that you're in, change directions to that direction. So, see, wow.
0:44:5.646 --> 0:44:9.406
Neville, Ryan L MAJ USARMY AI2C (USA)
See what happened. You got it.
0:44:12.376 --> 0:44:26.376
Neville, Ryan L MAJ USARMY AI2C (USA)
You know, just, I'm gonna graduate this is a great, great bridge, right? So, like, once you start typing something, you can just sort of see the real strong capital.
0:44:28.336 --> 0:44:33.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, yeah, so this next one we were seeing.
0:44:36.616 --> 0:44:43.816
Neville, Ryan L MAJ USARMY AI2C (USA)
That's the space, so you're gonna have to do that, so if you see the...
0:44:45.496 --> 0:44:48.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Facebook, yeah, interface, and here for.
0:44:52.56 --> 0:44:53.16
Neville, Ryan L MAJ USARMY AI2C (USA)
And now.
0:44:56.936 --> 0:44:57.256
Neville, Ryan L MAJ USARMY AI2C (USA)
It's.
0:44:58.376 --> 0:45:3.496
Neville, Ryan L MAJ USARMY AI2C (USA)
I think it's just escape, and then there's a radio, it's valid.
0:45:4.856 --> 0:45:5.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:45:7.736 --> 0:45:7.976
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:45:9.896 --> 0:45:11.576
Neville, Ryan L MAJ USARMY AI2C (USA)
It is.
0:45:15.96 --> 0:45:15.336
Neville, Ryan L MAJ USARMY AI2C (USA)
If.
0:45:20.536 --> 0:45:25.576
Neville, Ryan L MAJ USARMY AI2C (USA)
I have been trying to get her.
0:45:28.176 --> 0:45:46.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Probably there, your house, you know, in the quotation, that's what I do, it's the same my interview, right? Same it for months away, yeah, yeah, and then you can shoot Python random.
0:45:47.256 --> 0:45:49.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Who are you?
0:45:51.16 --> 0:45:54.296
Neville, Ryan L MAJ USARMY AI2C (USA)
But, but one of those, give you Python.
0:45:56.536 --> 0:45:57.576
Neville, Ryan L MAJ USARMY AI2C (USA)
Just type like one there.
0:45:58.616 --> 0:46:4.216
Neville, Ryan L MAJ USARMY AI2C (USA)
And I'm in space, but I'm exit out.
0:46:9.336 --> 0:46:10.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Space.
0:46:15.296 --> 0:46:20.536
Neville, Ryan L MAJ USARMY AI2C (USA)
It's ******* neat.
0:46:26.376 --> 0:46:27.96
Neville, Ryan L MAJ USARMY AI2C (USA)
Slash.
0:46:33.896 --> 0:46:39.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah. Tipsies there. That makes better struggles about five in a row.
0:46:49.656 --> 0:46:57.176
Neville, Ryan L MAJ USARMY AI2C (USA)
Couldn't view the file to just make sure it looks the way you expected, and yeah, it's in my spot.
0:46:59.96 --> 0:47:2.696
Neville, Ryan L MAJ USARMY AI2C (USA)
And then, and then script here.
0:47:5.336 --> 0:47:10.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Make sure that they're reading same file, right? Yeah, put file, yeah.
0:47:15.256 --> 0:47:18.96
Neville, Ryan L MAJ USARMY AI2C (USA)
That's fine. That's just an object. That's fine. Does that make sense?
0:47:22.856 --> 0:47:26.696
Neville, Ryan L MAJ USARMY AI2C (USA)
Yep, as you run it over and over, you should get different.
0:47:29.496 --> 0:47:30.56
Neville, Ryan L MAJ USARMY AI2C (USA)
I think.
0:47:37.16 --> 0:47:37.416
Neville, Ryan L MAJ USARMY AI2C (USA)
See.
0:47:38.696 --> 0:47:38.936
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
0:47:40.216 --> 0:47:40.616
Neville, Ryan L MAJ USARMY AI2C (USA)
True.
0:47:42.616 --> 0:47:43.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Now you do the sentence.
0:47:44.416 --> 0:47:58.776
Neville, Ryan L MAJ USARMY AI2C (USA)
What's that? It's been a while. Also, this is my first radio. I taught this stuff for like 3 years, so I've been doing it a long time. Is there? OK.
0:48:0.856 --> 0:48:1.256
Neville, Ryan L MAJ USARMY AI2C (USA)
Nice.
0:48:5.16 --> 0:48:5.816
Neville, Ryan L MAJ USARMY AI2C (USA)
So, yeah.
0:48:7.16 --> 0:48:7.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
0:48:8.336 --> 0:48:11.896
Neville, Ryan L MAJ USARMY AI2C (USA)
OK, but he says, ohh, yeah, so looking forward.
0:48:16.216 --> 0:48:16.936
Neville, Ryan L MAJ USARMY AI2C (USA)
Absolutely.
0:48:18.776 --> 0:48:20.216
Neville, Ryan L MAJ USARMY AI2C (USA)
This was a good time.
0:48:21.496 --> 0:48:21.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Is.
0:48:25.136 --> 0:48:26.136
Neville, Ryan L MAJ USARMY AI2C (USA)
So, it looks like...
0:48:33.416 --> 0:48:49.736
Neville, Ryan L MAJ USARMY AI2C (USA)
I got it. Yeah, so when you print out, go up here, do it on line thirty-two, put it on line thirty-two. Let's create a news line, and then let's just print one, so we can troubleshoot before.
0:48:51.216 --> 0:49:8.216
Neville, Ryan L MAJ USARMY AI2C (USA)
No, nobody knows. I think, yep. So, yeah, actually, through, yeah, for this, I have to, we could say this, but we'll still get, we'll get it.
0:49:9.456 --> 0:49:19.896
Neville, Ryan L MAJ USARMY AI2C (USA)
So, if we couldn't stop, we could, and so, like, for some reason, there's kind of...
0:49:22.376 --> 0:49:26.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Just one giant, yeah.
0:49:27.416 --> 0:49:38.536
Neville, Ryan L MAJ USARMY AI2C (USA)
So, click on your File Explorer, inside that file, so let's put a non-file to do any of this, yeah, here already.
0:49:41.976 --> 0:49:42.376
Neville, Ryan L MAJ USARMY AI2C (USA)
Is.
0:49:51.176 --> 0:50:3.456
Neville, Ryan L MAJ USARMY AI2C (USA)
So, that's all.
0:50:4.616 --> 0:50:18.936
Neville, Ryan L MAJ USARMY AI2C (USA)
But, um, scroll up through reading it. I can't do it. Yeah.
0:50:20.216 --> 0:50:40.376
Neville, Ryan L MAJ USARMY AI2C (USA)
It was once. Were you just in 65? That's awesome.
0:50:41.896 --> 0:51:0.696
Neville, Ryan L MAJ USARMY AI2C (USA)
Sure, I'm wondering if there's like, there's like, there's like, yeah, but I mean, yeah, there's like, there's like, and when it's...
0:51:4.616 --> 0:51:21.336
Neville, Ryan L MAJ USARMY AI2C (USA)
No, no, no, no, that's good. Let's go. That makes sense, 'cause that would not be a character that was making sense.
0:51:23.136 --> 0:51:40.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, it, it, it, but the pace looks like behind, and now it's like it's the X1 right, and it looks basically going wrong.
0:51:41.216 --> 0:51:45.936
Neville, Ryan L MAJ USARMY AI2C (USA)
Dang, that was such a small thing. Good catch, good catch.
0:51:49.576 --> 0:51:56.856
Neville, Ryan L MAJ USARMY AI2C (USA)
All right, let's jump right in. Let's jump into the next part of the lesson here. Any questions over kind of opening and manipulating files?
0:51:58.696 --> 0:51:59.896
Neville, Ryan L MAJ USARMY AI2C (USA)
All the questions?
0:52:1.16 --> 0:52:22.136
Neville, Ryan L MAJ USARMY AI2C (USA)
This is just an initial exposure. Again, we can open dot TXT files, we can open dot CSV files, we can open dot JSON files, we can open XML files. If you don't know what those are, those data types and those data formats, you're going to learn as part of your education over the next few months. They're just specific ways to save data.
0:52:22.296 --> 0:52:41.256
Neville, Ryan L MAJ USARMY AI2C (USA)
and you save them in these formats for different reasons. But again, we can open all those types of data in here. Let's say we wanted to open a.json. It would be as simple as just changing this to JSON. We would probably import the JSON module, which then allows us to quickly format our data as a JSON.
0:52:41.536 --> 0:52:50.696
Neville, Ryan L MAJ USARMY AI2C (USA)
And then we can throw it in there and load it, whatever. But just know that this is a standardized format here, regardless of data format. Okay.
0:52:54.136 --> 0:52:57.96
Neville, Ryan L MAJ USARMY AI2C (USA)
Alright, jumping into Jason, is your question?
0:53:6.296 --> 0:53:6.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Bob.
0:53:9.256 --> 0:53:29.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, so if you run, and I noticed this on some people, if you run your code from, say, the base repo, it's going to write the file where you run it from, right? So if I run my file in some random directory, run that Python script in some random directory, that's where it's going to write the file to. So you just need to be mindful where you're writing it to.
0:53:30.456 --> 0:53:47.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, yeah. A few people were like, where is this file? Where did it save? And it's because they were running that executable from a different location. Okay, which is just determined by this path right here, right down here at the bottom. That's telling me where I'm currently running my commands from.
0:53:49.896 --> 0:53:57.896
Neville, Ryan L MAJ USARMY AI2C (USA)
So in this case, if I run my script, it's going to write the file into lesson 5 Neville notes, or excuse me, just the lesson 5 folder there.
0:54:3.16 --> 0:54:13.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, yeah, watch if I go back one directory and then I run that same file. Let's try this Python. I might, this is a test here.
0:54:20.456 --> 0:54:21.416
Neville, Ryan L MAJ USARMY AI2C (USA)
This should put it.
0:54:25.896 --> 0:54:27.256
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, put it outside of.
0:54:28.616 --> 0:54:30.696
Neville, Ryan L MAJ USARMY AI2C (USA)
That folder, put it in the main Python folder.
0:54:35.376 --> 0:54:41.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Either you can specify it with an absolute directory right here, an absolute value or absolute path, excuse me, or...
0:54:42.976 --> 0:54:49.896
Neville, Ryan L MAJ USARMY AI2C (USA)
We could just make sure we run the code where we want to. Yeah. Yeah. Two things to note there. Yeah. Yep.
0:54:53.256 --> 0:54:55.576
Neville, Ryan L MAJ USARMY AI2C (USA)
Good, good little nuance things to notice.
0:54:57.416 --> 0:55:18.856
Neville, Ryan L MAJ USARMY AI2C (USA)
All right, there's two more modules I want to introduce you all to pretty quickly here. They're a little bit different from one another, but they help us traverse the file system and then we can do different operations on the file system with these modules. The OS module is the first one. This is a built-in module. It provides a way that we can interact with the underlying operating system.
0:55:19.96 --> 0:55:21.176
Neville, Ryan L MAJ USARMY AI2C (USA)
of the computer that we're on, okay?
0:55:23.96 --> 0:55:44.256
Neville, Ryan L MAJ USARMY AI2C (USA)
To use this, we just do import OS. Okay, import OS. That's how we import the operating system module. And it gives us a bunch of different methods that we can then use to create files, list the directories, update files, join file paths together, look at environment variables, et cetera.
0:55:44.456 --> 0:55:53.256
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, so again, this just gives us a way for our Python script to kind of look into the underlying system and manipulate the underlying system.
0:55:54.776 --> 0:56:14.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Similar to opening up the file context managers and manipulating those files, we can also manipulate things about the underlying computer itself. We can add folders, add files, look at what operating system is on the system that we're on, what platform we're on, et cetera.
0:56:14.296 --> 0:56:14.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Right.
0:56:20.256 --> 0:56:21.576
Neville, Ryan L MAJ USARMY AI2C (USA)
OK, here's an example.
0:56:24.56 --> 0:56:25.576
Neville, Ryan L MAJ USARMY AI2C (USA)
We just import OS.
0:56:27.656 --> 0:56:33.176
Neville, Ryan L MAJ USARMY AI2C (USA)
You can print, get current working directory. That'll tell you where you're at on the operating system.
0:56:34.336 --> 0:56:39.16
Neville, Ryan L MAJ USARMY AI2C (USA)
You can then move around with a change directory method, which is listed.
0:56:43.536 --> 0:56:45.16
Neville, Ryan L MAJ USARMY AI2C (USA)
I think coming up, hopefully.
0:56:46.456 --> 0:56:59.496
Neville, Ryan L MAJ USARMY AI2C (USA)
We can join some paths together, check if paths exist, etc. Okay. I'm going to cruise through this. There's a little practical at the end that you can do, but just note that that's what the OS module does for us. Okay. Here's some, here's some methods here.
0:57:1.816 --> 0:57:4.776
Neville, Ryan L MAJ USARMY AI2C (USA)
You can get the current working directory, you can change directory.
0:57:6.696 --> 0:57:15.256
Neville, Ryan L MAJ USARMY AI2C (USA)
et cetera, et cetera, right? So many of these commands, they mirror Linux command equivalents, right? Which we're already familiar with.
0:57:19.96 --> 0:57:26.456
Neville, Ryan L MAJ USARMY AI2C (USA)
And this is just a way that we can programmatically with Python add files, delete files, update files, etc.
0:57:29.856 --> 0:57:32.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Questions on this? Yeah, Jason.
0:57:34.456 --> 0:57:39.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Basically, translated from Python to whatever, yeah, exactly. Let's, let's I can pull up my...
0:57:40.816 --> 0:57:42.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Let me pull up my command prompt here.
0:57:43.696 --> 0:57:46.776
Neville, Ryan L MAJ USARMY AI2C (USA)
And I can do this real quickly, Python.
0:57:47.896 --> 0:57:51.256
Neville, Ryan L MAJ USARMY AI2C (USA)
I'm going to import OS, right? This is just an interactive terminal.
0:57:52.376 --> 0:58:1.576
Neville, Ryan L MAJ USARMY AI2C (USA)
Let me see where I'm at currently. Where am I operating from this? Okay, that's my username. I want to get on to the desktop.
0:58:4.456 --> 0:58:5.656
Neville, Ryan L MAJ USARMY AI2C (USA)
So...
0:58:9.16 --> 0:58:10.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Should be here somewhere.
0:58:12.56 --> 0:58:27.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Maybe. So that gives me a list. That's kind of ugly to look at. So I'm going to do for item in os.list directory. I'm just going to print the item so I can look at it in a more pretty way. Right? There we go.
0:58:31.176 --> 0:58:33.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Desktop is not in there.
0:58:34.376 --> 0:58:41.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Which is surprising. That's fine. I will just change directory to my documents.
0:58:44.96 --> 0:58:46.456
Neville, Ryan L MAJ USARMY AI2C (USA)
Verify that that happens or happened.
0:58:47.896 --> 0:58:49.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, now I'm in documents.
0:59:33.936 --> 0:59:34.936
Neville, Ryan L MAJ USARMY AI2C (USA)
Following along.
0:59:37.336 --> 0:59:38.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Sorry about that.
0:59:41.896 --> 0:59:44.696
Neville, Ryan L MAJ USARMY AI2C (USA)
O, if I go to my documents here.
0:59:46.56 --> 0:59:48.776
Neville, Ryan L MAJ USARMY AI2C (USA)
And now in my command prompt with Python.
0:59:50.616 --> 0:59:51.176
Neville, Ryan L MAJ USARMY AI2C (USA)
Ohh.
0:59:52.376 --> 0:59:59.576
Neville, Ryan L MAJ USARMY AI2C (USA)
I can do like an OS dot make directory test Python directory.
1:0:5.216 --> 1:0:6.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Does not work.
1:0:7.136 --> 1:0:7.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Should work.
1:0:9.16 --> 1:0:9.896
Neville, Ryan L MAJ USARMY AI2C (USA)
Find the right spot.
1:0:26.136 --> 1:0:26.696
Neville, Ryan L MAJ USARMY AI2C (USA)
There it is.
1:0:27.656 --> 1:0:28.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Try again.
1:0:31.336 --> 1:0:34.696
Neville, Ryan L MAJ USARMY AI2C (USA)
So I can show here that I can create a folder with Python.
1:0:35.696 --> 1:0:36.936
Neville, Ryan L MAJ USARMY AI2C (USA)
There we go, it worked.
1:0:39.816 --> 1:0:40.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Good.
1:0:44.456 --> 1:0:56.376
Neville, Ryan L MAJ USARMY AI2C (USA)
That's the OS module. I'm going to run you through this next module. It's the pathlib module. This one's a little different. It creates a like an object-oriented approach to file system paths.
1:0:57.816 --> 1:0:59.576
Neville, Ryan L MAJ USARMY AI2C (USA)
So we can create a path.
1:1:0.776 --> 1:1:8.856
Neville, Ryan L MAJ USARMY AI2C (USA)
Using this method, and then we can do things based on that path. So let me kind of demonstrate here. I can import pathlib.
1:1:10.216 --> 1:1:14.136
Neville, Ryan L MAJ USARMY AI2C (USA)
So now I can do this P equals path.
1:1:15.896 --> 1:1:22.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Lib.path gotta call it that way, and I'm gonna use my current working directory as the path.
1:1:26.136 --> 1:1:44.296
Neville, Ryan L MAJ USARMY AI2C (USA)
And if I put in the commands right, that will work. Note that I can, so now I have a path object. Okay, so what I've done here is I'm using the current working directory that I'm getting from the OS module. I'm feeding it into this pathlib.path method, and I'm getting a path object.
1:1:45.256 --> 1:2:7.416
Neville, Ryan L MAJ USARMY AI2C (USA)
To verify that this is a path object, I can use the type command. We can check the data type, right? And this will say, hey, this is a class pathlib object. That's what it is. It's a path object. That gives us the ability to use different built-in methods to manipulate it. So now I can use some of these.
1:2:9.976 --> 1:2:13.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Methods like make directory, P.make directory.
1:2:13.976 --> 1:2:21.16
Neville, Ryan L MAJ USARMY AI2C (USA)
and it will actually make a directory, okay? Or rename or exist, et cetera, right?
1:2:23.256 --> 1:2:27.736
Neville, Ryan L MAJ USARMY AI2C (USA)
So this would be like P dot make directory hello.
1:2:30.616 --> 1:2:31.256
Neville, Ryan L MAJ USARMY AI2C (USA)
Solid.
1:2:33.856 --> 1:2:34.616
Neville, Ryan L MAJ USARMY AI2C (USA)
That's my.
1:3:5.176 --> 1:3:8.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Not exactly sure how to use this method. We can figure it out here.
1:3:11.776 --> 1:3:13.176
Neville, Ryan L MAJ USARMY AI2C (USA)
Look at this GT real quick.
1:3:22.776 --> 1:3:23.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Oh, okay.
1:3:33.816 --> 1:3:34.616
Neville, Ryan L MAJ USARMY AI2C (USA)
Try that.
1:4:6.856 --> 1:4:25.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, that's one way to list things. So anyway, these are two different approaches to exploring the underlying operating system. Again, the OS module is maybe a little more intuitive because we've used similar Linux command, whereas this pathlib module, we're using path objects to traverse the...
1:4:26.96 --> 1:4:29.736
Neville, Ryan L MAJ USARMY AI2C (USA)
file system and manipulate the file system. Good.
1:4:31.16 --> 1:4:38.56
Neville, Ryan L MAJ USARMY AI2C (USA)
That's really the only two things I wanted to expose you to. What we created, if you go to your...
1:4:41.256 --> 1:4:42.856
Neville, Ryan L MAJ USARMY AI2C (USA)
Lesson 5 folder.
1:4:50.616 --> 1:4:53.176
Neville, Ryan L MAJ USARMY AI2C (USA)
We created this file IO markdown.
1:4:54.376 --> 1:5:4.296
Neville, Ryan L MAJ USARMY AI2C (USA)
So this file IO markdown just kind of challenges you to do different things that we've kind of exposed you to here. So if we go look at the markdown.
1:5:8.776 --> 1:5:10.456
Neville, Ryan L MAJ USARMY AI2C (USA)
close out all these real quick.
1:5:13.856 --> 1:5:17.976
Neville, Ryan L MAJ USARMY AI2C (USA)
It's going to tell you to clone a repo from here.
1:5:19.136 --> 1:5:26.136
Neville, Ryan L MAJ USARMY AI2C (USA)
And then use OS and pathlib modules to change the contents of that repo. OK.
1:5:27.296 --> 1:5:40.696
Neville, Ryan L MAJ USARMY AI2C (USA)
I'm going to give you all 15 minutes to kind of work through these exercises, and then that'll be it for today. But any kind of questions, burning questions for me on the context managers, like with open, the OS module, or the pathlib module?
1:5:45.176 --> 1:6:2.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay, take 15 minutes to work through some of these hands-on exercises. I can float around if you have any questions or issues, but this is kind of exploratory. So if you don't get it to work right away, just know that that's kind of the point, okay? It's something you got to figure out, and this is just an exposure, okay?
1:7:17.336 --> 1:7:17.576
Neville, Ryan L MAJ USARMY AI2C (USA)
This.
1:10:15.896 --> 1:10:16.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Just.
1:10:20.136 --> 1:10:20.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Right.
1:10:23.256 --> 1:10:26.616
Neville, Ryan L MAJ USARMY AI2C (USA)
What's up?
1:10:28.656 --> 1:10:29.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Hello.
1:10:30.56 --> 1:10:30.616
Neville, Ryan L MAJ USARMY AI2C (USA)
Like.
1:10:31.976 --> 1:10:32.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Changes.
1:10:33.536 --> 1:10:34.536
Neville, Ryan L MAJ USARMY AI2C (USA)
She is the only.
1:10:39.16 --> 1:10:39.176
Neville, Ryan L MAJ USARMY AI2C (USA)
Ohh.
1:10:40.376 --> 1:10:40.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
1:10:48.136 --> 1:10:48.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
1:11:5.736 --> 1:11:6.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
1:11:7.96 --> 1:11:7.736
Neville, Ryan L MAJ USARMY AI2C (USA)
The person.
1:11:14.296 --> 1:11:14.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Sing.
1:11:20.656 --> 1:11:21.936
Neville, Ryan L MAJ USARMY AI2C (USA)
Move to.
1:11:23.56 --> 1:11:23.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Two.
1:11:24.856 --> 1:11:29.96
Neville, Ryan L MAJ USARMY AI2C (USA)
But we have to make it on Microsoft.
1:11:31.736 --> 1:11:32.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Listen.
1:11:35.336 --> 1:11:35.816
Neville, Ryan L MAJ USARMY AI2C (USA)
What's that?
1:11:41.816 --> 1:11:42.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Ohh, awesome.
1:11:44.616 --> 1:11:44.856
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
1:11:51.256 --> 1:11:51.616
Neville, Ryan L MAJ USARMY AI2C (USA)
See.
1:11:52.936 --> 1:11:53.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
1:12:9.496 --> 1:12:10.176
Neville, Ryan L MAJ USARMY AI2C (USA)
Thank you.
1:12:22.616 --> 1:12:22.896
Neville, Ryan L MAJ USARMY AI2C (USA)
Two.
1:12:26.456 --> 1:12:27.936
Neville, Ryan L MAJ USARMY AI2C (USA)
Sorry, tell me a second.
1:12:35.176 --> 1:12:35.576
Neville, Ryan L MAJ USARMY AI2C (USA)
You.
1:12:37.656 --> 1:12:38.16
Neville, Ryan L MAJ USARMY AI2C (USA)
English.
1:12:41.176 --> 1:12:41.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
1:12:43.336 --> 1:12:43.536
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
1:12:44.616 --> 1:12:44.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
1:12:47.496 --> 1:12:47.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
1:13:0.776 --> 1:13:1.16
Neville, Ryan L MAJ USARMY AI2C (USA)
One.
1:13:19.976 --> 1:13:20.576
Neville, Ryan L MAJ USARMY AI2C (USA)
This is.
1:13:23.896 --> 1:13:24.216
Neville, Ryan L MAJ USARMY AI2C (USA)
It.
1:13:28.496 --> 1:13:28.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Did you?
1:13:37.416 --> 1:13:41.336
Neville, Ryan L MAJ USARMY AI2C (USA)
This, this, and it's time.
1:13:54.666 --> 1:13:56.186
Neville, Ryan L MAJ USARMY AI2C (USA)
I got to get back here.
1:13:57.736 --> 1:13:58.136
Neville, Ryan L MAJ USARMY AI2C (USA)
It's.
1:13:59.16 --> 1:13:59.416
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
1:14:2.456 --> 1:14:2.776
Neville, Ryan L MAJ USARMY AI2C (USA)
St.
1:14:5.976 --> 1:14:7.376
Neville, Ryan L MAJ USARMY AI2C (USA)
I'll.
1:14:11.976 --> 1:14:30.496
Neville, Ryan L MAJ USARMY AI2C (USA)
I think you're out of you're out of date. You're so you're listening to Grace file. I know it should be less than follow. Yeah. Yeah.
1:14:30.776 --> 1:14:32.536
Neville, Ryan L MAJ USARMY AI2C (USA)
I know.
1:14:37.736 --> 1:14:38.776
Neville, Ryan L MAJ USARMY AI2C (USA)
I think.
1:14:42.376 --> 1:14:59.416
Neville, Ryan L MAJ USARMY AI2C (USA)
So, read your, read your here, what is the name of the project is, right? And so, it's looking for a variable, we need to put.
1:14:59.496 --> 1:14:59.736
Neville, Ryan L MAJ USARMY AI2C (USA)
Or.
1:15:1.56 --> 1:15:1.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
1:15:6.96 --> 1:15:6.216
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
1:15:10.56 --> 1:15:10.616
Neville, Ryan L MAJ USARMY AI2C (USA)
It's not.
1:15:12.696 --> 1:15:34.96
Neville, Ryan L MAJ USARMY AI2C (USA)
OK, so our system. So the big function of extensive change.
1:15:35.296 --> 1:15:35.816
Neville, Ryan L MAJ USARMY AI2C (USA)
Hold on.
1:15:40.536 --> 1:15:46.776
Neville, Ryan L MAJ USARMY AI2C (USA)
So, yeah, I mean, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, yeah.
1:15:59.816 --> 1:16:2.776
Neville, Ryan L MAJ USARMY AI2C (USA)
And I understood that.
1:16:5.176 --> 1:16:5.496
Neville, Ryan L MAJ USARMY AI2C (USA)
No.
1:16:7.256 --> 1:16:7.976
Neville, Ryan L MAJ USARMY AI2C (USA)
It's.
1:16:16.56 --> 1:16:17.936
Neville, Ryan L MAJ USARMY AI2C (USA)
Ohh, there's no one.
1:16:21.896 --> 1:16:23.96
Neville, Ryan L MAJ USARMY AI2C (USA)
So, I missed that.
1:16:26.536 --> 1:16:26.856
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
1:16:31.176 --> 1:16:35.96
Neville, Ryan L MAJ USARMY AI2C (USA)
I mean.
1:16:43.656 --> 1:16:44.136
Neville, Ryan L MAJ USARMY AI2C (USA)
But...
1:16:47.656 --> 1:16:50.416
Neville, Ryan L MAJ USARMY AI2C (USA)
I am going to respond.
1:16:52.576 --> 1:16:55.896
Neville, Ryan L MAJ USARMY AI2C (USA)
Actually, we have.
1:16:57.976 --> 1:17:12.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Ohh, I'm sure, yeah, it would have to.
1:17:14.376 --> 1:17:14.696
Neville, Ryan L MAJ USARMY AI2C (USA)
It.
1:17:19.816 --> 1:17:25.976
Neville, Ryan L MAJ USARMY AI2C (USA)
See how you're in this, so you might have to, so.
1:17:27.736 --> 1:17:27.816
Neville, Ryan L MAJ USARMY AI2C (USA)
If.
1:17:33.896 --> 1:17:34.56
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
1:17:36.616 --> 1:17:36.776
Neville, Ryan L MAJ USARMY AI2C (USA)
See.
1:17:40.216 --> 1:17:40.296
Neville, Ryan L MAJ USARMY AI2C (USA)
Ohh.
1:17:43.936 --> 1:17:44.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
1:17:49.336 --> 1:17:49.496
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
1:17:52.936 --> 1:17:54.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah, this is.
1:17:57.576 --> 1:18:6.296
Neville, Ryan L MAJ USARMY AI2C (USA)
I think we've stashed it, which is on how it's been.
1:18:15.296 --> 1:18:21.296
Neville, Ryan L MAJ USARMY AI2C (USA)
It is checked, it did not exceed if they did not.
1:18:22.776 --> 1:18:23.96
Neville, Ryan L MAJ USARMY AI2C (USA)
It.
1:18:33.896 --> 1:18:34.456
Neville, Ryan L MAJ USARMY AI2C (USA)
I think.
1:18:38.576 --> 1:18:38.696
Neville, Ryan L MAJ USARMY AI2C (USA)
Good.
1:18:40.536 --> 1:18:40.856
Neville, Ryan L MAJ USARMY AI2C (USA)
Sheila.
1:18:47.536 --> 1:18:47.656
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
1:18:56.856 --> 1:18:57.16
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
1:18:58.776 --> 1:18:59.256
Neville, Ryan L MAJ USARMY AI2C (USA)
OK.
1:19:9.896 --> 1:19:10.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Big.
1:19:13.496 --> 1:19:13.896
Neville, Ryan L MAJ USARMY AI2C (USA)
Hey.
1:19:20.56 --> 1:19:20.376
Neville, Ryan L MAJ USARMY AI2C (USA)
Hmm.
1:19:24.616 --> 1:19:24.856
Neville, Ryan L MAJ USARMY AI2C (USA)
Thank you.
1:19:29.216 --> 1:19:29.336
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
1:19:32.456 --> 1:19:32.776
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.
1:19:35.56 --> 1:19:35.256
Neville, Ryan L MAJ USARMY AI2C (USA)
No.
1:19:39.656 --> 1:19:40.176
Neville, Ryan L MAJ USARMY AI2C (USA)
Sorry.
1:19:52.256 --> 1:19:52.376
Neville, Ryan L MAJ USARMY AI2C (USA)
Yeah.
1:19:54.56 --> 1:19:54.376
Neville, Ryan L MAJ USARMY AI2C (USA)
No.
1:20:0.936 --> 1:20:1.136
Neville, Ryan L MAJ USARMY AI2C (USA)
Sure.
1:20:7.296 --> 1:20:12.856
Neville, Ryan L MAJ USARMY AI2C (USA)
The time is currently 1230. Do you all want half an hour for lunch or an hour?
1:20:14.336 --> 1:20:33.616
Neville, Ryan L MAJ USARMY AI2C (USA)
People have spoken. This was a break in my brain. Come back at 1330. Got this going, not understanding. Yeah, this is what's happening. So, there, yeah, type for a second.
1:20:34.496 --> 1:20:42.16
Neville, Ryan L MAJ USARMY AI2C (USA)
So, we could do this, bring it back in my system.
1:20:45.776 --> 1:20:45.936
Neville, Ryan L MAJ USARMY AI2C (USA)
Okay.