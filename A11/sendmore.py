str1=str(input("String 1: "))
str2=input("String 2: ")
str3=input("Result  : ")

str0=str1+str2+str3
a=[]
for i in range(len(str0)):
	if(str0[i] not in a):	
		a.append(str0[i])
print(a)

c=0
for i1 in range(1,10):
	for i2 in range(10):
		if(i2 != i1 ):
			for i3 in range(10):
				if(i3 != i1 and i3 != i2):
					for i4 in range(10):
						if(i4 != i1 and i4 != i2 and i4 != i3):
							for i5 in range(1,10):
								if(i5 != i1 and i5 != i2 and i5 != i3 and i5 != i4):
									for i6 in range(10):
										if(i6 != i1 and i6 != i2 and i6 != i3 and i6 != i4 and i6 != i5):
											for i7 in range(10):
												if(i7 != i1 and i7 != i2 and i7 != i3 and i7 != i4 and i7 != i5 and i7!=i6):
													for i8 in range(10):
														if(i8 != i1 and i8 != i2 and i8 != i3 and i8 != i4 and i8 != i5 and i8!=i6 and i8!=i7):
													
															s1=1000*i1 + 100*i2 + 10*i3 +i4
															#print(s1)
															s2=1000*i5 + 100*i6 + 10*i7 +i2
															#print(s2)
															s3=10000*i5 + 1000*i6 + 100*i3 +10*i2 + i8
															#print(s3)
															if(s1+s2==s3):
																print("%d\n%d\n------\n%d\n-----\n" %(s1,s2,s3))
                                                 		        
                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                												                    