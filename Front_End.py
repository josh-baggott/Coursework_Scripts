# imports
import tkinter as tk
from tkinter import ttk, messagebox

from PIL import ImageTk

from Graph_Display import *
from Questions import *


# functions

def reactions():
    """
    This function takes the image of the shortest route from the Graph_Display.py script and displays it on a canvas. Also, it removes all
    of the text from the reaction information labels so the new information can be added in a separate function.

    :return: N/A
    """
    g = ReactionGraph(startNode=interface.start_combo.get(), endNode=interface.end_combo.get())

    try:
        shortest_path = g.find_shortest_path()
    except ValueError as e:
        messagebox.showerror("Error", e)

        return None

    try:
        display_graph(shortest_path)
    except ValueError as e:
        messagebox.showerror("Error", e)

        return None

    reaction_list = g.display_info(shortest_path)

    for label in interface.reaction_number_labels:
        label.configure(text="")
    for label in interface.reaction_name_labels:
        label.configure(text="")
    for label in interface.reaction_reagents_labels:
        label.configure(text="")
    for label in interface.reaction_products_labels:
        label.configure(text="")
    for label in interface.reaction_conditions_labels:
        label.configure(text="")

    interface.reaction_info_header.configure(text="Reaction Info")

    GUI.image = ImageTk.PhotoImage(file="DisplayedGraph.png")
    GUI.canvasImage = interface.canvas.create_image(174, 120, image=GUI.image)
    interface.canvas.itemconfig(GUI.canvasImage, image=GUI.image)

    for i in range(0, len(shortest_path) - 1):
        reaction = reaction_list[i]

        interface.reaction_number_labels[i].configure(text="Reaction " + str(i + 1))
        interface.reaction_name_labels[i].configure(text="Name: " + g.reactions[reaction][0])
        interface.reaction_reagents_labels[i].configure(text="Reagents: " + g.reactions[reaction][1])
        interface.reaction_products_labels[i].configure(text="Products: " + g.reactions[reaction][2])
        interface.reaction_conditions_labels[i].configure(text="Conditions: " + g.reactions[reaction][3])
        interface.reaction_break_labels[i].configure(text="    ")


def display_quiz():
    """


    :return: N/A
    """

    global quiz_length

    try:
        quiz_length = Question.validate_input(interface.length_spinbox.get())
    except ValueError as e:
        tk.messagebox.showerror("Error", e)

        interface.length_submit.config(state="normal")
        interface.quiz_submit.config(state="disabled")

        return None

    interface.length_submit.config(state="disabled")
    interface.quiz_submit.config(state="normal")
    interface.length_spinbox.config(state="disabled")

    global question_list
    question_list = []

    for i in range(0, quiz_length):
        question_list.append(Question())

    generated_numbers_list = generate_numbers(quiz_length)

    count = 0

    for question in question_list:
        question.configure_questions(question, str(generated_numbers_list[count]))

        count += 1

    interface.score_label.config(text="")

    for i in range(0, 4):
        interface.question_labels[i].config(text="")
        interface.answer_A_radio_buttons[i].config(text="", value=None)
        interface.answer_B_radio_buttons[i].config(text="", value=None)
        interface.answer_C_radio_buttons[i].config(text="", value=None)
        interface.answer_D_radio_buttons[i].config(text="", value=None)
        interface.verdict_labels[i].config(text="")

    for i in range(0, quiz_length):
        interface.question_labels[i].config(text=question_list[i].question)
        interface.answer_A_radio_buttons[i].config(text=question_list[i].answer_A, value=question_list[i].answer_A, state="normal")
        interface.answer_B_radio_buttons[i].config(text=question_list[i].answer_B, value=question_list[i].answer_B, state="normal")
        interface.answer_C_radio_buttons[i].config(text=question_list[i].answer_C, value=question_list[i].answer_C, state="normal")
        interface.answer_D_radio_buttons[i].config(text=question_list[i].answer_D, value=question_list[i].answer_D, state="normal")


def mark():
    """


    :return: N/A
    """
    for i in range(0, 4):
        interface.answer_A_radio_buttons[i].config(state="disabled")
        interface.answer_B_radio_buttons[i].config(state="disabled")
        interface.answer_C_radio_buttons[i].config(state="disabled")
        interface.answer_D_radio_buttons[i].config(state="disabled")

    question = Question()

    user_inputs = []

    for i in range(0, quiz_length):
        user_inputs.append(interface.answers[i].get())

    score, percentage, correct_answers, incorrect_answers, incorrect_questions_corrections = question.mark_questions(user_inputs, question_list)

    interface.score_label.config(text="Score: " + str(score) + "/" + str(quiz_length) + "            " + str(percentage) + "%")

    for correct in correct_answers:
        interface.verdict_labels[int(correct) - 1].config(text="CORRECT", font="Helvetica 10 bold", foreground="green")

    count = 0

    for incorrect in incorrect_answers:
        interface.verdict_labels[int(incorrect) - 1].config(text="INCORRECT      Correct Answer: " + str(incorrect_questions_corrections[count]), font="Helvetica 10 bold", foreground="red")
        count += 1

    interface.quiz_submit.config(text="Reset", command=reset)


def reset():
    """


    :return: N/A
    """

    interface.quiz_submit.config(text="Submit Answers", state="disabled", command=mark)
    interface.length_submit.config(state="normal")
    interface.length_spinbox.config(state="normal")

    interface.score_label.config(text="")

    for i in range(0, 4):
        interface.question_labels[i].config(text="")
        interface.answer_A_radio_buttons[i].config(text="", value="", state="disabled")
        interface.answer_B_radio_buttons[i].config(text="", value="", state="disabled")
        interface.answer_C_radio_buttons[i].config(text="", value="", state="disabled")
        interface.answer_D_radio_buttons[i].config(text="", value="", state="disabled")
        interface.verdict_labels[i].config(text="")


# classes


class GUI:

    def __init__(self, master):
        """
        This function initialises the interface by creating all of the widgets and placing them on their respective tabs

        :param master: The main window of the interface
        """
        self.master = master
        master.title("Organic Chemistry Aid")

        master.tab_parent = ttk.Notebook(master)

        master.geometry("1400x875")

        master.iconbitmap("benzene.ico")

        self.compound_list = ["Carboxylic Acid", "Ester", "Sodium Carboxylate Salt", "Other Ester", "Alcohol", "Hydroxy Halide", "Polymer", "Acyl or Acid Halide", "Silver Mirror", "Aldehyde", "Diol", "Brick Red Precipitate", "Iodoform", "Alkene", "Alkane", "Bright Orange Solid", "Ketone", "Dihalogenoalkane", "Carbon Dioxide + Water + Energy", "Secondary or Tertiary Amide", "Primary Amide", "Nitrile", "Hydroxynitrile", "Halogenoalkane", "Copper Complex Ion", "Amine", "Salts", "Secondary Amine", "Primary Alcohol", "Secondary Alcohol", "Grignard Reagent", "Tertiary Alcohol"]

        self.tab1 = ttk.Frame(master.tab_parent)
        self.tab2 = ttk.Frame(master.tab_parent)

        master.tab_parent.add(self.tab1, text="Learn")
        master.tab_parent.add(self.tab2, text="Quiz")
        master.tab_parent.pack(expand=1, fill='both')

        # tab 1

        self.start_label = ttk.Label(self.tab1, text="Enter Start Compound:", font='Helvetica 18 bold')
        self.start_label.grid(row=0, column=1)

        self.start_combo = ttk.Combobox(self.tab1, values=self.compound_list, width=30)
        self.start_combo.grid(row=1, column=1)

        self.end_label = ttk.Label(self.tab1, text="Enter End Compound:", font='Helvetica 18 bold')
        self.end_label.grid(row=3, column=1)

        self.end_combo = ttk.Combobox(self.tab1, values=self.compound_list, width=30)
        self.end_combo.grid(row=4, column=1)

        self.submit = ttk.Button(self.tab1, text="Submit", command=reactions)
        self.submit.grid(row=6, column=1)

        self.separator = ttk.Separator(self.tab1, orient="horizontal")
        self.separator.grid(row=7, column=1)

        self.canvas = tk.Canvas(self.tab1, width=348, height=250)
        self.canvas.grid(row=9, column=1)

        # reaction info labels

        self.reaction_info_header = ttk.Label(self.tab1, text="", font='Helvetica 20 bold')
        self.reaction_info_header.grid(row=10, column=1)

        self.reaction_number_labels = []
        self.reaction_name_labels = []
        self.reaction_reagents_labels = []
        self.reaction_products_labels = []
        self.reaction_conditions_labels = []
        self.reaction_break_labels = []

        r = 12
        c = 0

        for i in range(1, 5):
            self.reaction_number_labels.append((ttk.Label(self.tab1, text="", font='Helvetica 14 bold')))
            self.reaction_number_labels[i - 1].grid(row=r, column=c)

            self.reaction_name_labels.append((ttk.Label(self.tab1, text="")))
            self.reaction_name_labels[i - 1].grid(row=r + 1, column=c)

            self.reaction_reagents_labels.append((ttk.Label(self.tab1, text="")))
            self.reaction_reagents_labels[i - 1].grid(row=r + 2, column=c)

            self.reaction_products_labels.append((ttk.Label(self.tab1, text="")))
            self.reaction_products_labels[i - 1].grid(row=r + 3, column=c)

            self.reaction_conditions_labels.append((ttk.Label(self.tab1, text="")))
            self.reaction_conditions_labels[i - 1].grid(row=r + 4, column=c)

            self.reaction_break_labels.append(ttk.Label(self.tab1, text=""))
            self.reaction_break_labels[i - 1].grid(row=r + 5, column=c)

            if (r == 12 or r == 19) and c == 0:
                c += 2
            elif r == 12 and c == 2:
                r += 7
                c -= 2

        # tab 2

        self.length_label = ttk.Label(self.tab2, text="Enter Quiz Length - Between 1 & 4", font='Helvetica 18 bold')
        self.length_label.pack()

        self.length_spinbox = ttk.Spinbox(self.tab2, from_=1, to=4, wrap=True)
        self.length_spinbox.pack()

        self.breaker(self.tab2)

        self.length_submit = ttk.Button(self.tab2, text="Submit", command=display_quiz)
        self.length_submit.pack()

        self.breaker(self.tab2)

        self.quiz_header = ttk.Label(self.tab2, text="Questions", font='Helvetica 18 bold')
        self.quiz_header.pack()

        self.score_label = ttk.Label(self.tab2, text="")
        self.score_label.pack()

        self.breaker(self.tab2)

        self.question_labels = []
        self.verdict_labels = []
        self.answer_A_radio_buttons = []
        self.answer_B_radio_buttons = []
        self.answer_C_radio_buttons = []
        self.answer_D_radio_buttons = []
        self.answers = []

        for answer in range(0, 4):
            answer = tk.StringVar()
            self.answers.append(answer)

        for i in range(1, 5):
            self.question_labels.append(ttk.Label(self.tab2, text="", font="Helvetica 11 bold"))
            self.question_labels[i - 1].pack()

            self.answer_A_radio_buttons.append(ttk.Radiobutton(self.tab2, text="", variable=self.answers[i - 1], value=None, state="disabled"))
            self.answer_A_radio_buttons[i - 1].pack()

            self.answer_B_radio_buttons.append(ttk.Radiobutton(self.tab2, text="", variable=self.answers[i - 1], value=None, state="disabled"))
            self.answer_B_radio_buttons[i - 1].pack()

            self.answer_C_radio_buttons.append(ttk.Radiobutton(self.tab2, text="", variable=self.answers[i - 1], value=None, state="disabled"))
            self.answer_C_radio_buttons[i - 1].pack()

            self.answer_D_radio_buttons.append(ttk.Radiobutton(self.tab2, text="", variable=self.answers[i - 1], value=None, state="disabled"))
            self.answer_D_radio_buttons[i - 1].pack()

            self.verdict_labels.append(ttk.Label(self.tab2, text=""))
            self.verdict_labels[i - 1].pack()

            self.breaker(self.tab2)

        self.quiz_submit = ttk.Button(self.tab2, text="Submit Answers", state="disabled", command=mark)
        self.quiz_submit.pack()

    # formatting functions

    def breaker(self, tab):
        break_label = ttk.Label(tab, text="")
        break_label.pack()


# main

if __name__ == "__main__":
    root = tk.Tk()
    interface = GUI(root)
    root.mainloop()
