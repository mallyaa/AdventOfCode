#/usr/bin/env python
# coding: utf-8

# In[6]:


with open('Day3.txt') as f:
    nums = [l.strip() for l in f.readlines()]
digits = list(zip(*nums))
gamma = ''.join([max(set(d), key=d.count) for d in digits])
epsilon = ''.join(['1' if c == '0' else '0' for c in gamma])
print('Power consumption: ', end='')
print(int(gamma, 2)*int(epsilon, 2))

def find_rating(lines, keep_fn):
  digit = 0
  width = len(lines[0])
  while len(lines)>1:
    ones = sum([1 for line in lines if line[digit] == '1'])
    keep_chr = keep_fn(len(lines)-ones, ones)
    lines = [l for l in lines if l[digit] == keep_chr]
    digit +=1
  return int(lines[0],2)
oxy = find_rating(nums, lambda zeroes, ones: '1' if ones >= zeroes else '0')
co2 = find_rating(nums, lambda zeroes, ones: '0' if zeroes <= ones else '1')
print('Life support rating: ', end='')
print(oxy*co2)


# In[ ]:




