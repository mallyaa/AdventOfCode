#!/usr/bin/env python
# coding: utf-8

# In[6]:


from collections import namedtuple
if __name__ == '__main__':
    with open("Day2.txt", "r") as f:
        commands = namedtuple('command', ['direction', 'magnitude'])
        arr = map(lambda x: commands(x.split()[0], int(x.split()[1])), f.read().splitlines())
        hor, depth = 0, 0
        for command in arr:
            if command.direction=="forward":
                hor += command.magnitude
            elif command.direction=="up":
                depth -= command.magnitude
            elif command.direction=="down":
                depth += command.magnitude
        print(hor*depth)


# In[7]:


if __name__ == '__main__':
    with open("Day2.txt", "r") as f:
        arr = map(lambda x: (x.split()[0], int(x.split()[1])), f.read().splitlines())
        hor, depth, aim = 0, 0, 0
        for dir, magnitude in arr:
            if dir=="forward":
                hor += magnitude
                depth += aim*magnitude
            elif dir=="up":
                aim -= magnitude
            elif dir=="down":
                aim += magnitude
        print(hor*depth)


# In[ ]:




