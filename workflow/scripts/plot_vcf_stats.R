# Plot some vcf statistics

# Sorry that the script is in such a terrible shape xD I will clean it up tomorrow :P 
library(ggplot2)

dataset = 'survivor'

if (dataset == 'sniffles'){
  vcf_csv_link = '~/Downloads/samplot_sniffles_input_hg002_3_4_complete.csv'
  vars = read.table(vcf_csv_link, sep=',', header=T)
  vars$length = vars$END - vars$START
  vars = vars[vars$length <= 50, ]
  #vars = vars[vars$TYPE != 'BND', ]
  
} else if (dataset == 'survivor'){
  vcf_csv_link = '~/Downloads/samplot_survivor_input_hg002_3_4.csv'
  vars = read.table(vcf_csv_link, sep=',', header=T)
  
}



vars$length = vars$END - vars$START

stats = table(vars$MENDELIAN_VIOLATION)
pct_violators = round(as.numeric((stats[2] / (stats[1] + stats[2])) * 100), 1)


#ggplot(vars) + geom_point(aes(x=length, y=MENDELIAN_VIOLATION)) + scale_x_log10()

#ggplot(vars) + geom_boxplot(aes(x=MENDELIAN_VIOLATION, y=length)) + scale_y_log10()


barplot = ggplot(vars) + geom_bar(aes(x=TYPE, fill=MENDELIAN_VIOLATION), width = 0.5) + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6)) + 
  labs(title=paste0("DATASET: ",dataset, "\nSVs total: ", stats[1] + stats[2], " \nMendelian inconsitent: " , stats[2], " (", pct_violators, "%)"),
       subtitle="") 
barplot
