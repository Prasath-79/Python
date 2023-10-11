# nested list
lis=[1,['hi','hello',['welcome','bye'],'thanks'],2,3,4,['how','are','you'],5]
#bye
lis[1][2][1]
'bye'
#are
lis[-2][-2]
'are'
lis[1].append('ok')
print(lis)
[1, ['hi', 'hello', ['welcome', 'bye'], 'thanks', 'ok'], 2, 3, 4, ['how', 'are', 'you'], 5]
lis[1][2].append(6)
print(lis)
[1, ['hi', 'hello', ['welcome', 'bye', 6], 'thanks', 'ok'], 2, 3, 4, ['how', 'are', 'you'], 5]
lis[-6][-3].append(6)
print(lis)
[1, ['hi', 'hello', ['welcome', 'bye', 6, 6], 'thanks', 'ok'], 2, 3, 4, ['how', 'are', 'you'], 5]
lis[-6][-3].pop(-1)
6
print(lis)
[1, ['hi', 'hello', ['welcome', 'bye', 6], 'thanks', 'ok'], 2, 3, 4, ['how', 'are', 'you'], 5]
lis[1].insert(-1,7)
print(lis)
[1, ['hi', 'hello', ['welcome', 'bye', 6], 'thanks', 7, 'ok'], 2, 3, 4, ['how', 'are', 'you'], 5]
del lis[1][2]
print(lis)
[1, ['hi', 'hello', 'thanks', 7, 'ok'], 2, 3, 4, ['how', 'are', 'you'], 5]
lis[1].extend([['welcome', 'bye', 6]])
print(lis)
[1, ['hi', 'hello', 'thanks', 7, 'ok', ['welcome', 'bye', 6]], 2, 3, 4, ['how', 'are', 'you'], 5]
lis[-2].remove('are')
print(lis)
[1, ['hi', 'hello', 'thanks', 7, 'ok', ['welcome', 'bye', 6]], 2, 3, 4, ['how', 'you'], 5]
print(len(lis))
7
print(len(lis[1][5]))
3
lis[-2].sort(reverse=True)
print(lis)
[1, ['hi', 'hello', 'thanks', 7, 'ok', ['welcome', 'bye', 6]], 2, 3, 4, ['you', 'how'], 5]
