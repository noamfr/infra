import pickle
import logging
from typing import List
from os import path
from .timer import Timer


class Pipeline_Executor:
    def __init__(self, pipeline_class, steps: List, save_history: bool, save_state: bool, pickle_path: str,
                 job_key: str):
        self.pipeline = pipeline_class
        self.steps = steps
        self.save_history = save_history
        self.save_state = save_state
        self.pickle_path = pickle_path
        self.job_key = job_key

    def execute(self):
        self.__load_pipeline()
        self.__run_steps()

    def __run_steps(self):
        for step in self.steps:
            step = step.__name__
            timer = Timer()
            logging.info("================ Executing: " + step + " ================")
            print("================ Executing: " + step + " ================")
            getattr(self.pipeline, step)()

            logging.info("================ Finished running: " + step + " ================")
            timer.stop_timer()
            print("================ Finished running: " + step + " ================")
            timer.print_elapsed_time()

            self.__save_pipeline_if_needed(step)

    def __save_pipeline_if_needed(self, step):
        if self.save_state:
            logging.info("================ Saving: " + step + " to pickle ================")
            print("================ Saving: " + step + " to pickle ================")
            with open(path.join(self.pickle_path, self.job_key + '.pickle'), 'wb') as handle:
                pickle.dump(obj=self.pipeline, file=handle)

    def __load_pipeline(self):
        logging.info("================ Loading pickle file ===========")
        print("================ Loading pickle file ===========")

        if self.save_history:
            try:
                file = open(path.join(self.pickle_path, self.job_key + '.pickle'), 'rb')
                self.pipeline = pickle.load(file)
            except:
                pass
