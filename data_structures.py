
class DataStructures:
    # strHello = ""
    def __init__(self):
        strHello = "Hello, there!"
        print(strHello)

    def section1_1(self):
        ## SECTION 1.1
        #You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.
        p = (4, 5)
        x, y = p
        print (x, y)

        # _ will just discard the value stored in that place
        t= (2, 'broth')
        _, r = t
        print(r)

    def section1_2(self):
        ## SECTION 1.2
        #You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a too many values to unpack exception.
        record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
        name, email, *phone_numbers = record
        print (phone_numbers)


        records = [
            ('doi', 2, 3),
            ('patru', 5),
            ('doi', 9, 'zece')
        ]

        def do_doi(x, y):
            print('doi', x, y)

        def do_altceva(x):
            print('altceva', x)

        for tag, *values in records:
            if tag == "doi":
                do_doi(*values)
            else:
                do_altceva(*values)

        #---it can be used also when splitting
        line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
        uname, *fields, homedir, sh = line.split(':')
        print(fields)

        #---it also works with lists
        items = [2, 4, 7, 8, 5]
        head, *middle, tail = items

        print(middle)

    ## SECTION 1.3
        #You want to keep a limited history of the last few items seen during iteration or during some other kind of processing.
    def section1_3(self):
        from collections import deque

        def search(lines, pattern, history):
            #We're creating a queue...
            previous_lines = deque(maxlen=history)
            for line in lines:
                if pattern in line:
                    #...returning the lines containing the so called pattern, actually the keywork searched
                    yield line, previous_lines
                previous_lines.append(line)

        #opening file
        f = open('section1_3.txt')
        #...and looking for the keyword
        for line, prevLines in search(f, 'Python', 5):
            #it first prints the lines before it
            for pline in prevLines:
                print(pline, end='')
            #then the line containing the keyword
            print(line, end='')
            #then it highlights it
            print('-'*20)
    ## SECTION 1.4
        #You want to make a list of the largest or smallest N items in a collection.
    def section1_4(self):
        import heapq
        nums = [1, 4, 2, 11, 53, 63, 77, 37, 84, 22, 3, 8, 5]
        print("Largest 3 numbers for", str(nums), "are", heapq.nlargest(3, nums))
        print("Smallest 3 numbers for", str(nums), "are", heapq.nsmallest(3, nums))

        data =[
            {'name': 'Aurelian Temisan', 'power': 200, 'nickname': '2peu'},
            {'name': 'Daniel Iordachioaie', 'power': 300, 'nickname': 'my little pony'},
            {'name': 'Cristi Minculescu', 'power': 5000, 'nickname': 'Ficatzel'},
            {'name': 'Rudarel', 'power': 10000, 'nickname': 'Macarena'},
            {'name': 'Nelu Vlad', 'power': 4500, 'nickname': 'Azur'},
            {'name': 'Mihai Constantinescu', 'power': 400, 'nickname': 'Maidanezofilul'}
        ]
        print('Top 3 singers by power from this bunch', 'are', heapq.nlargest(3, data, key=lambda s: s['power']))
        print('worst 3 singers by power from this bunch', 'are', heapq.nlargest(3, data, key=lambda s: s['power']))

    ## SECTION 1.5
        #You want to implement a queue that sorts items by a given priority and always returns the item with the highest priority on each pop operation.
    def section1_5(self):
        import heapq

        #Designing a class for the queue
        class PriorityQueue:
            def __init__(self):
                self._queue = []
                self._index = 0

            #pusing in the queue, with negative priority so that we get the highest first.
            def push(self, item, priority):
                heapq.heappush(self._queue, (-priority, self._index, item))
                self._index+=1

            def pop(self):
                return heapq.heappop(self._queue)[-1]

        class Item:
            def __init__(self, name):
                self.name=name

            def __repr__(self):
                return 'Item({!r})'.format(self.name)

        q=PriorityQueue()
        q.push(Item('foo'), 1)
        q.push(Item('bar'), 4)
        q.push(Item('cry'), 3)
        q.push(Item('grok'), 1)
        print(q.pop())
