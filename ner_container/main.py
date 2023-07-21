import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from simpletransformers.ner import NERModel,NERArgs

data = pd.read_csv("file.csv",encoding="latin1")
data.head(30)
data =data.fillna(method ="ffill")
data.head(30)
data["Sentence #"] = LabelEncoder().fit_transform(data["Sentence #"])
data.head(30)
data.rename(columns={"Sentence #":"sentence_id","Word":"words","Tag":"labels"}, inplace =True)
data["labels"] = data["labels"].str.upper()
X= data[["sentence_id","words"]]
Y =data["labels"]
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size =0.2)
#building up train data and test data
train_data = pd.DataFrame({"sentence_id":x_train["sentence_id"],"words":x_train["words"],"labels":y_train})
test_data = pd.DataFrame({"sentence_id":x_test["sentence_id"],"words":x_test["words"],"labels":y_test})
train_data
label = data["labels"].unique().tolist()
label
args = NERArgs()
args.num_train_epochs = 5
args.learning_rate = 1e-4
args.train_batch_size = 32
args.eval_batch_size = 32
args.overwrite_output_dir = True
args.best_model_dir = "best_model/"
args.eval_during_training = True
args.save_best_model =True
args.eval_during_training = True
model = NERModel('bert', 'bert-base-cased',labels=label,args =args, use_cuda=False)
model.train_model(train_data,eval_data = test_data,acc=accuracy_score)
result, model_outputs, preds_list = model.eval_model(test_data)
prediction, model_output = model.predict(["Je voudrais partir de Toulon a Montpellier"])
print(prediction)