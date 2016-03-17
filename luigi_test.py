"""
https://www.uppmax.uu.se/automating-workflows-using-the-luigi-batch-workflow-system


Perceived differences between dtool and luigi:

    - dtool allows for a configurations to be inherited by child properties, in
      luigi it seems like these must be spelled out in the requires method. In the case where
      these params change, you would need to modify the entire heirarchy or requires heirarchy
      that you get for free with dtool.

    - dtool is built around the idea of a core object and computing properties
      of that object.
    It then assumes that you have many instances of that object, so it
      computes the same property in batch when executing tasks that involve more
      than one object.
    In contrast it seems as if luigi is built around the idea of a task and
      this task represents a task a high level job (like aggregating this weeks
      top artists) rather than a job at the level of an object proprty (which
      has a one-to-one mapping with a root object).
    Dtool does support the idea of aggregated reports, but it must be
      specified as an aggregation of root object properties (which are computed
      on the fly as necessary).


    - A luigi task does subsampleing, in dtool we assume you have already sampled the correct
    input and are passing that along into the model.

    - luigi outputs each run task to its own file. In contrast it seems like a
    dtool table is the similar analogy to a task, but all runs of a task are
    stored in the same file (by default).

    - I think you should be able to replace task functions with luigi run functions.
    self.input() is akin to getting input passed into you via the function signature.

    - Depc supports on the fly lookup and inspection of little pieces of Tasks.

    - Luigi does not seem to remember the input to the task or distinguish between a task
    with a one-to-one mapping between input and output and a many-to-one mapping needed for
    model training.

       * maybe an interval parameter is sort of like many-to-one?

Ideas:

    If we could define a luigi.Task for every table we might be able to implement the backend of dtool in luigi.
    We could handle the configuration inheritence for luigi.
    We would be the benefit of luigi's scheduler.
    Would not have to work with luigi's input / output.

"""
import luigi


class AnnotTask(luigi.Task):
    """
    Task that representes the "always available"  root of the depcache tree.
    """
    root_rowid = luigi.Parameter()


class ChipTask(luigi.Task):
    annot_param = luigi.TaskParameter(AnnotTask)
    #upstream_task = luigi.Parameter()
    #def requires(self):
    #    pass

    def requires(self):
        return self.annot_param
        #return AnnotTask(root_rowid=1)

    #def output(self):
    #        #return MockFile("SimpleTask", mirror_on_stderr=True)

    def run(self):
        annot = self.requires()
        print('annot = %r' % (annot,))
        pass
        #_out = self.output().open('w')
        #_out.write(u"Hello World!\n")
        #_out.close()


if __name__ == '__main__':
    x = ChipTask()
    x.run()
    #luigi.run(ChipTask)
