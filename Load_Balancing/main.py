#declaring the variable used in the program

M=0
no_of_services=0
service_ids=[]
robots_availability=[]
available_robots=[]
service_book={}
work_load={}

#taking input of all the required data 
def get_all_input():
    global M,workload,robots_availability

    # taking input of number of robots
    while True:
        try:
            M=int(input('\nEnter the number of Robots, M :'))
            if M>0:
                workload=[[0,0]]*M
                robots_availability=[1]*M
                for i in range(M):
                    service_book[f'robot{i+1}']=[] 
                    work_load[f'robot{i+1}']=0
                break

            else:
                print('\nNumber of Robots can not be negative!!')
        except ValueError:
            print('\nEnter a valid input!!')

    #taking input of number of serviced 
    while True:
        try:
            no_of_services=int(input('\nEnter the number of Services :'))
            if no_of_services>=0:
                break
            else:
                print('\nNumber of Robots can not be negative!!')
        except ValueError:
            print('\nEnter a valid input!!')
    
    # taking input of service ids of those services
    for i in range(no_of_services):
        while True:
            try:
                str=input(f'\nEnter the Service-Id of Service-{i+1} :')
                if str.endswith(('0','1','2','3','4','5','6','7','8','9')):
                    service_ids.append(str)
                    break
                else:
                    print('\nService-Id ends with numerals.')

            except ValueError:
                print('\nEnter a valid input!!')

    # taking input of number of robots which are unavailable to work (due to maintenance or Error occurance) 
    while True:
        try:
            no_of_unavailable_robots=int(input('\nEnter the no of Unavailable Robots (Under maintenance or Encounterred an error)\n(0 if all robots available) :'))
            if 0<= no_of_unavailable_robots<=M:
                break
            else:
                print(f'\nNumber of unavailable Robots can\'t go out of range of 0 to {M}!')
        except ValueError:
            print('\nEnter a valid input!!')

    # taking input of robot id for the unavailable robots
    for i in range(no_of_unavailable_robots):
        while True:
            try:
                c=int(input(f'\nEnter the Robot Number of unavailable_robot-{i+1} :'))
                if 0<c<=M:
                    robots_availability[c-1]=0
                    break
                else:
                    print(f'\nRobot numbers are from 1 to {M}')
            except ValueError:
                print('\nEnter a valid input!!')
    

# this function is used to assign services to those robots which are available ,leaving behind the unavailable robots
def assign_services_to_robots():
    global available_robots,robots_availability

    available_robots.extend(i  for i in range(M) if robots_availability[i]==1)
    for service_no,service_id in enumerate(service_ids):
        service_book[f'robot{available_robots[service_no%len(available_robots)]+1}'].append(service_id)
        work_load[f'robot{available_robots[service_no%len(available_robots)]+1}']+=1


#this is for runnig all the required funtion to run our program
def run():
    get_all_input()
    assign_services_to_robots()
    print(service_book)
    print(work_load)

#calling run program
run()