import random

import matplotlib.pyplot as plt


class TossProgram:
    def __init__(self) -> None:
        # record T and H
        self.total_tosses = 0
        self.total_T_start = 0
        self.total_H_start = 0
        self.toss_T_T = 0
        self.toss_H_H = 0
        self.total_same_toss = 0
        self.probability_list = []
        self.toss_turn_list = []
        #define list for starting with T
        self.toss_T_turn_list=[]
        self.probability_T_list=[]
        #define list for starting with H
        self.toss_H_turn_list=[]
        self.probability_H_list=[]

    def simulate_tosses(self):
        while True:
            # Generate the initial toss.
            initial_toss = random.choice(["T", "H"])
            # record the initial tost
            if initial_toss == "T":
                self.total_T_start += 1
                self.toss_T_turn_list.append(self.total_T_start)
            else:
                self.total_H_start += 1
                self.toss_H_turn_list.append(self.total_H_start)
            # Ask for user input on a new line for clarity.
            toss_result = input("Enter toss result (T or H, anything else to exit): ")
            if toss_result != "T" and toss_result != "H":
                #pop the result for exiting
                if initial_toss == "T":
                    self.toss_T_turn_list.pop()
                else:
                    self.toss_H_turn_list.pop()
                print("Exiting.")
                break
            #add total toss
            self.total_tosses += 1
            self.toss_turn_list.append(self.total_tosses)
            if initial_toss == toss_result:
                self.total_same_toss += 1
                if initial_toss == "H":
                    self.toss_H_H += 1
                else:
                    self.toss_T_T += 1
            #calculate the probability for tail and head
            if initial_toss=='T':
                #calculate tail probability
                probability_T=self.toss_T_T / self.total_T_start
                self.probability_T_list.append(probability_T)
            else:
                #calculate head probability
                probability_H=self.toss_H_H / self.total_H_start
                self.probability_H_list.append(probability_H)
            
            # calculate probability
            probability = self.total_same_toss / self.total_toss
            self.probability_list.append(probability)

    def parse_old_result(self, filename: str):
        # initialize old result file
        file1 = open(filename, "r")
        # read the result file line by line
        lines = file1.readlines()
        line_shift = False
        initial_toss: str
        toss_result: str
        for line in lines:
            if not line_shift:
                # the third last character of the line is initial toss for odd line
                initial_toss = line[-3]
                if initial_toss == "T":
                    self.total_T_start += 1
                    self.toss_T_turn_list.append(self.total_T_start)
                else:
                    self.total_H_start += 1
                    self.toss_H_turn_list.append(self.total_H_start)
                line_shift = True
            else:
                # the second last character of the line is initial toss for odd line
                toss_result = line[-2]
                if toss_result != "T" and toss_result != "H":
                    #pop the result for exiting
                    if initial_toss == "T":
                        self.toss_T_turn_list.pop()
                    else:
                        self.toss_H_turn_list.pop()
                    print("Exiting.")
                    break
                # add one toss
                self.total_tosses += 1
                self.toss_turn_list.append(self.total_tosses)
                # print(f"initial toss:{initial_toss}, toss result:{toss_result}")
                if initial_toss == toss_result:
                    self.total_same_toss += 1
                    if initial_toss == "T":
                        self.toss_T_T += 1
                                               
                    else:
                        self.toss_H_H += 1
                if initial_toss=='T':
                    #calculate tail probability
                    probability_T=self.toss_T_T / self.total_T_start
                    self.probability_T_list.append(probability_T)
                else:
                    #calculate head probability
                    probability_H=self.toss_H_H / self.total_H_start
                    self.probability_H_list.append(probability_H)
                # calculate total probability
                probability = self.total_same_toss / self.total_tosses
                self.probability_list.append(probability)
                line_shift = False

    def print_result(self):
        print(f"Total number of tosses is {self.total_tosses}")
        print(f"Times with same probability:{self.total_same_toss}")
        probability_T_T = self.toss_T_T / self.total_T_start
        probability_H_H = self.toss_H_H / self.total_H_start
        print(f"Probability of 'T' start leading to 'T' result: {probability_T_T:.2f}")
        print(f"Probability of 'H' start leading to 'H' result: {probability_H_H:.2f}")

    def plot_total(self):
        plt.plot(self.toss_turn_list, self.probability_list)
        plt.title("toss_turn vs probability")
        plt.show()

    def plot_T(self):
        plt.plot(self.toss_T_turn_list, self.probability_T_list)
        plt.title("toss turn tail vs probability")
        plt.show()

    def plot_H(self):
        plt.plot(self.toss_H_turn_list, self.probability_H_list)
        plt.title("toss turn head vs probability")
        plt.show()


def main():
    p = TossProgram()
    p.parse_old_result("old_result.txt")
    p.print_result()
    p.plot_total()
    p.plot_T()
    p.plot_H()


if __name__ == "__main__":
    main()
