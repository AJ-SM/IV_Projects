import numpy as np

#defining the variables used 
N=0
prob=[]
impact_factor=[]
S=0
range_of_N=[1,100]
range_of_prob_value=[0.00,1.00]
range_of_impact_factor=[1,10000]
range_of_threshold_value=[0.00,1.00]
Pcb=[]
truth_table=[]
win_loss_arrangements=[]
impact_factor_sums_for_win_loss_arrangements=[]

#defining the functions

#this function is used to take input of number of battles
def get_no_of_battles():
    global N,range_of_N
    while True:
        try:
            N=int(input('Enter the total number of Battles, N (Integer): '))
            if range_of_N[0]<=N<=range_of_N[1]:
                break
            else:
                print(f'Please enter a number between {range_of_N[0]} to {range_of_N[1]}')
        except ValueError:
            print('Enter a valid Input!')
            pass

#this function is used to take input of probability of winning the battle corresponding to a battle
def get_prob_for_winning():
    global N,prob,range_of_prob_value
    for i in range(N):
        while True:
            try:
                num = float(input(f'Enter probability of winnig the battle for battle {i+1} :'))
                if round(num, 2) == num and  range_of_prob_value[0]<= num <= range_of_prob_value[1]:
                    prob.append(num)
                    break
                else:
                    print(f"Please enter a number with up to 2 decimal places in range of {range_of_prob_value[0]} to {range_of_prob_value[1]}.")
            except ValueError:
                print("Please enter a valid Input!")


#this function is used to take input of impact factors of corresponding battle
def get_impact_factors():
    global N,range_of_impact_factor,impact_factor
    for i in range(N):
        while True:
            try:
                num=int(input(f'Enter the impact factor of battle {i+1} :'))
                if range_of_impact_factor[0] <= num <= range_of_impact_factor[1]:
                    impact_factor.append(num)
                    break
                else:
                    print(f'Please enter a number between {range_of_impact_factor[0]} to {range_of_impact_factor[1]}')
            except ValueError:
                print('Enter a valid Input!')
                pass


#this function is used to take input of threshold value (S)
def get_threshold_value():
    global S,range_of_threshold_value
    while True:
        try:
            num = float(input(f'Enter the Threshold value, S :'))
            if round(num, 2) == num and  range_of_threshold_value[0]<= num <= range_of_threshold_value[1]:
                S=num
                break
            else:
                print(f"Please enter a number with up to 2 decimal places in range of {range_of_threshold_value[0]} to {range_of_threshold_value[1]}.")
        except ValueError:
            print("Please enter a valid Input!")


#just return the probability as it is ,as the input is itself the winnig probability
def prob_of_winning(num):
    return num

#this function is used to get the probability of losing a battle (as sum of winning and losing battle will be 1)
def prob_of_losing(num):
    return 1-num


#this function is used to make truth table for n number of variables, which is further used to have various possibilites of combination of winning and losing battles, here 0 is used for denoting defeat and 1 is used to denote win in a battle 

# there would be 2 pow N number of possible ways for analysing the given scenario.
def make_truth_table(no_of_variables):
    global truth_table

    for i in range(no_of_variables):
        truth_table.extend(([[0]]*(pow(2,no_of_variables-i-1)),[[1]]*(pow(2,no_of_variables-i-1)))*pow(2,i))
    required_table=[]

    for sublist in truth_table:
        for elem in sublist:
            required_table.append(elem)
    
    truth_table=np.array(required_table).reshape(no_of_variables,-1)
    


#this function is used to generate the sum of impact factors of winning battles,winning battles are those which we get through the truth table as calculated earlier
def generate_impact_factor_sums():
    global truth_table,Pcb,win_loss_arrangements

    for i in range(len(truth_table[0])):
        win_loss_arrangements.append(truth_table[:,i])
        Pcb.append(0)
        impact_factor_sums_for_win_loss_arrangements.append(0)
        count=0
        sum1=0
        sum2=0
        for j in win_loss_arrangements[i]:
            if j==0:                                        #checking if battle lost
                sum1-=prob_of_winning(prob[count])
            else:                                           #checking if battle won
                sum1+=prob_of_winning(prob[count])
                sum2+=impact_factor[count]
            Pcb[i]=sum1/(count+1)
            if Pcb[i]<0:                                    #resetting the Pcb value if it falls beyond zero
                Pcb[i]=0
            count+=1
        impact_factor_sums_for_win_loss_arrangements[i]=sum2    
        if not Pcb[i]<S:   #considering the whole way of fighting the battle as wrong.by eliminating the impact factor sum produced here
            impact_factor_sums_for_win_loss_arrangements[i]=0


def get_data():
    get_no_of_battles()
    get_prob_for_winning()
    get_impact_factors()
    get_threshold_value()


def run():
    get_data()
    make_truth_table(N)
    generate_impact_factor_sums()
    print(f'maximum sum of impact factors for given data is: {max(impact_factor_sums_for_win_loss_arrangements)}')


run()