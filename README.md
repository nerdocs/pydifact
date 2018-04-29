## pydifact - A Python EDIFACT library


#### Preamble

This is a port of [metroplex-systems/edifact](https://github.com/metroplex-systems/edifact) to Python. Thanks here at the start to [Craig Duncan](https://github.com/duncan3dc) for this cool piece of software. Porting was like a breeze due to the high code quality there. All credits for the initial code here go to him, I just did the translation to Python 3.

#### Why another EDIFACT library?

Because I did not find a decent UN/EDIFACT library for Python, so I decided to port one of the available good PHP libraries to Python. Here is the result.

ATM this is a Work In Progress, feel free to help.

#### Usage

To read a message from a file or from a string, take the `Message` class:

    from pydifact.Message import Message
    message = Message.from_file("/pydifact/data/order.edi");
    message = Message:from_str("UNA:+,? 'UNH+1+ORDERS:D:96A:UN:EAN008'")

Now you can iter over the segments:

    for segment in message.get_all_segments():
        print('Segment code: {}, content: {}'.format(
            segment.tag, segment.get_all_elements()))


            
