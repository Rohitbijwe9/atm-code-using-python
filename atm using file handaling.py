







 
# Atm exception handaling andfile handaling


class IntError:
    pass
import datetime

x=datetime.datetime.now()


pas=input('please enter your password:')

f=open('C:\\Users\\Admin\\Desktop\\DEMO\\atmpass.txt','r')
p1=f.read()
f.close()
if p1==pas:
    #while True:
        try:
            while True:
 
                c=int(input('0-change password\n1-add balance\n2-check balance\n3-withdrawl balance\n4-mini statment\n5-exit\nchoose the option:'))
                if c==0:
            
     
                    pas1=input('please enter your old password:')
        
            
                    f=open('C:\\Users\\Admin\\Desktop\\DEMO\\atmpass.txt','r')
                
                    p2=f.read()
                    if p2==pas1:
                        print('password must be 4 digit')
                        pa=input('Enter new password:')
                        pa1=input('confirm your password:')
                        if pa==pa1:
                            pass
                            if len(str(pa))==4:
                                f=open('C:\\Users\\Admin\\Desktop\\DEMO\\atmpass.txt','w')

                                f.write(pa)
                                f.close()
                                print('passwor generate sucessfulyy..')
                                continue

                            else:
                                print('passwprd less than or greater than 4 digit')
                                continue
                        else:
                            print('password do not match')
                            continue

                    else:
                        print('your old pass and new pass not match')
                        continue

                            
        
                if c==1:
                    f=open('C:\\Users\\Admin\\Desktop\\DEMO\\atm.txt','r')

                    ab=(input('enter the deposit amount:'))
                    f2=f.read()
                    ti=int(ab)+int(f2)
                    ts=str(ti)
                    f.close()
                    f=open('C:\\Users\\Admin\\Desktop\\DEMO\\atm.txt','w')
                    f.write(ts)
                    f.close()
                    print('balance deposit sucessfuly...')

                    
                    f1=open('C:\\Users\\Admin\\Desktop\\DEMO\\atmstatment.txt','a')
                    
                    t1=str(x)+' '+'credit:+ '+ab
                    f1.write('\n'+t1)
                    f1.close()
            
     

                
                    
         
                    
                    
                    continue
            
                
                elif c==2:
               
             
                    f=open('C:\\Users\\Admin\\Desktop\\DEMO\\atm.txt','r')
                    print('available balance is:',f.readline())
                    f.close()
                    continue
                elif c==3:
                    
                    f=open('C:\\Users\\Admin\\Desktop\\DEMO\\atm.txt','r')
                    ab1=f.read()
                    ab=int(ab1)
                    w1=input('enter withdrawl amount:')
                    w=int(w1)
                    if ab>w:
                        print('withdrawl sucessfuly...')
                        cb=ab-w
                        cb1=str(cb)
                        print('current balance is:',cb)
                    else:
                        print('insuficiant balnce...')
                        continue
                    f.close()
                    f=open('C:\\Users\\Admin\\Desktop\\DEMO\\atm.txt','w')
                    f.write(cb1)
                    f.close()
                    f1=open('C:\\Users\\Admin\\Desktop\\DEMO\\atmstatment.txt','a')
                    t1=str(x)+' '+'debit:- '+w1

                    f1.write('\n'+t1)
                    f1.close()
                    continue
            

                elif c==4:
                    f=open('C:\\Users\\Admin\\Desktop\\DEMO\\atmstatment.txt','r')
                    print(f.read())
                    f.close()
                   
                    continue
                    
                elif c==5:
                    
                    
                    
                    break


                else:
                    print('invalid option')
                    #break
                

        except ValueError:
            print('choose option only take int value')
            #break
        except Exception:
            print('choose option only take int value')
            #break
        except IntError as msg:
            print(msg)
            #break
        else:
            print('Transaction Sucessful')
        finally:
            print('program end')
                


                

else:
    print('incorect password.')
    
