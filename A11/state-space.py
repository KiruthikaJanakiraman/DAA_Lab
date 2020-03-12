str1="shanta"
str2="meena"
str3="gandhi"

str0=str1+str2+str3
a=[]
for i in range(len(str0)):
	if(str0[i] not in a):	
		a.append(str0[i])
print(a)

c=0
for s in range(1,10):
	for h in range(10):
		if(h != s ):
			for a in range(10):
				if(a != s and a != h):
					for n in range(10):
						if(n != s and n != h and n != a):
							for t in range(1,10):
								if(t != s and t != h and t != a and t != n):
									for m in range(1,10):
										if(m != s and m != h and m != a and m != n and m != t):
											for e in range(10):
												if(e != s and e != h and e != a and e != n and e != t and e!=m):
													for g in range(1,10):
														if(g != s and g != h and g != a and g != n and g != t and g!=m and g!=e):
															for d in range(10):
																if(d != s and d != h and d != a and d != n and d != t and d!=m and d!=e and d!=g):
																	for i in range(10):
																		if(i != s and i != h and i != a and i != n and i != t and i!=m and i!=e and i!=g and i!=d):
													
																			shanta=100000*s + 10000*h + 1000*a +100*n + 10*t + a
															#print(s1)
																			meena=10000*m + 1000*e + 100*e + 10*n + a
															#print(s2)
																			gandhi=100000*g + 10000*a + 1000*n +100*d + 10*h + i
															#print(s3)
																			if(shanta + meena == gandhi):
																				print("s-%d h-%d a-%d n-%d t-%d m-%d e-%d g-%d d-%d i-%d" %(s,h,a,n,t,m,e,g,d,i))
																				print("%d\n %d\n------\n%d\n------\n" %(shanta,meena,gandhi))

                                                 		        
                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                												                    