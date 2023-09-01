# Here are the commands that Mauricio, Raj and Wolfy used to check the two de-novo SVs on chr7 and chr17
# 1st Sep 2023, 12:30 Germany time

# Make samplots
samplot plot     -n HG002_son HG003_father HG004_mother     -b HG002.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam       HG003.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam       HG004.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam     -o de_novo/de_novo_literature_lift.png     -c chr17     -s 53340465     -e 53340571     -t DEL    --ignore_hp

samplot plot     -n HG002_son HG003_father HG004_mother     -b HG002.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam       HG003.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam       HG004.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam     -o de_novo/de_novo_1_sniffles.png     -c chr7     -s 142786194     -e 142796810     -t DEL    --ignore_hp


# To subset vcfs to look at the variants in our data, we used
bcftools view -r chr17:53340465-53340571 sniffles_HG002-3-4_multisample_mendelannotate.vcf.gz
bcftools view -r chr7:142757892-142824789 sniffles_HG002-3-4_multisample_mendelannotate.vcf.gz
