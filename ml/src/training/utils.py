from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from pandas import DataFrame

class Trainer:
    def __init__(self, 
                 estimator,
                 df:DataFrame,
                 target:str,
                 params:dict) -> None:
        
        self.estimator = estimator(**params)
        self.target = target        
        self.params = params

        self.X = df.drop(target,axis=1)
        self.y = df[target]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2
        )

        self._y_pred = None
        self._accuracy_metrices = None

    @property
    def y_pred(self):
        if self._y_pred is None:
            raise ValueError("Model not yet fitted")
        return self._y_pred
    
    @y_pred.setter
    def y_pred(self, value):
        self._y_pred = value

    @property
    def accuracy_metrices(self):
        if self._accuracy_metrices is None:
            raise ValueError("Model not yet fitted")
        return self._accuracy_metrices
    
    @accuracy_metrices.setter
    def accuracy_metrices(self,value):
        self._accuracy_metrices = value

    def fit(self) -> None:
        self.estimator.fit(self.X_train, self.y_train)

        self.y_pred = self.estimator.predict(self.X_test)
        self.self_test = self.estimator.predict(self.X_train)

        self.accuracy_metrices = {
            "accuracy_test": accuracy_score(self.y_test, self.y_pred),
            "accuracy_train": accuracy_score(self.y_train, self.self_test),
            "precision_test": precision_score(self.y_test, self.y_pred),
            "precision_train": precision_score(self.y_train, self.self_test),
            "recall_test":recall_score(self.y_test, self.y_pred),
            "recall_train":recall_score(self.y_train, self.self_test),
            "f1_test":f1_score(self.y_test, self.y_pred),
            "f1_train":f1_score(self.y_train, self.self_test)
        }
        