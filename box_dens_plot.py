import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sys import argv
from utils import load_csv, filter_dataframe
import seaborn as sns

def kernel_density(df: pd.DataFrame, course: str):
	"""Plots the kernel density plot for the specific course"""
	df[course].plot.kde()
	plt.title(course)
	plt.show()
	
def box_plot(orig_df: pd.DataFrame, norm_df: pd.DataFrame, course: str):
	"""Plots the box plot for the specific course"""
	plot = sns.boxplot(x=orig_df['Hogwarts House'], y=norm_df[course])
	plot.set_title(course)
	plt.show()

def plot_all_courses(orig_df, norm_df):
	"""Plots the box plot and kernel density plot for each courses"""
	for course in norm_df.columns:
		box_plot(orig_df, norm_df, course)
		kernel_density(norm_df, course)

def main():
	if len(argv) == 2:
		dataframe = load_csv(argv[1])
		if dataframe is None:
			print ("Input a valid file to run the program")
			return
	else:
		print ("Input the dataset to run the program.")
		return
	
	courses_df = filter_dataframe(dataframe)
	plot_all_courses(dataframe, courses_df)

if __name__ == "__main__":
    main()