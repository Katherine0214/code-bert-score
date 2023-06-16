################################# lang='en' ###########################
import code_bert_score

# hide the loading messages
import logging
import transformers
transformers.tokenization_utils.logger.setLevel(logging.ERROR)
transformers.configuration_utils.logger.setLevel(logging.ERROR)
transformers.modeling_utils.logger.setLevel(logging.ERROR)


import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["xtick.major.size"] = 0
rcParams["xtick.minor.size"] = 0
rcParams["ytick.major.size"] = 0
rcParams["ytick.minor.size"] = 0

rcParams["axes.labelsize"] = "large"
rcParams["axes.axisbelow"] = True
rcParams["axes.grid"] = True

from code_bert_score import score

with open("pred_GLM.txt", encoding = "utf-8") as f:
    cands = [line.strip() for line in f]

with open("refs.txt", encoding = "utf-8") as f:
    refs = [line.strip() for line in f]

P, R, F1, F3 = score(cands, refs, lang='en', verbose=True)
print(F1)
print(f"System level F1 score: {F1.mean():.3f}")
print(f"System level F3 score: {F3.mean():.3f}")





##################################################################
# from code_bert_score import score
# from transformers import AutoTokenizer, AutoModelForMaskedLM

# tokenizer = AutoTokenizer.from_pretrained("codebert-python")
# model = AutoModelForMaskedLM.from_pretrained("codebert-python")


# with open("hyps.txt") as f:
#     cands = [line.strip() for line in f]

# with open("refs.txt") as f:
#     refs = [line.strip() for line in f]

# (P, R, F), hashname = score(cands, refs, lang="en", return_hash=True)
# print(f"{hashname}: P={P.mean().item():.6f} R={R.mean().item():.6f} F={F.mean().item():.6f}")

