import os
from datetime import datetime
import numpy as np
import wandb
import imageio


class _WANDBLogger():
    def __init__(self):
        # logs
        self.log_id = datetime.now().strftime("%Y%m%d-%H%M")
        self.log_dir = os.path.join(
                os.getcwd(),
                'logs',
                'wandb_runs',
                self.log_id
            )
        self.param_dir = os.path.join(self.log_dir, "params")
        self.img_dir = os.path.join(self.log_dir, "img")
        self.vid_dir = os.path.join(self.log_dir, "vid")
        #
        self._create_dir(self.log_dir)
        self._create_dir(self.param_dir)
        self._create_dir(self.img_dir)
        self._create_dir(self.vid_dir)
        #
        self.run = wandb.init(
                dir=self.log_dir,
                project="Athena",
                name="New",
                entity="mo379",
            )

    def _create_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _log(self, dictionary):
        self.run.log(dictionary)

    def _log_arr_video(self, name, arr, full_sys_path):
        imageio.mimsave(
                os.path.join(self.log_dir, f"videos/{self.log_id}.gif"),
                [np.array(img) for i, img in enumerate(arr) if i % 1 == 0],
                fps=30
        )
        self.run.log({
            name: wandb.video(
                os.path.join(self.log_dir, f"videos/{self.log_id}.gif"),
                full_sys_path,
                fps=30,
                format='gif'
            )
        })

    def _log_params(self, name, params):
        self.run.log({
            name: wandb.Histogram(params)
        })

    def _finish(self):
        self.run.finish()
