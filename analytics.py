import os
import matplotlib.pyplot as plt
import operator

class Sessions:
    def __init__(self, root_path):
        self.root_path = root_path

    def get_session_paths(self):
        session_paths = []

        for session_index in range(1, self.get_dirs_count(self.root_path)):
            if os.path.isdir(self.get_session_path(session_index)):
                session_paths.append(self.get_session_path(session_index))
        
        return session_paths

    def get_dirs_count(self, path):
        return len(os.listdir(path))

    def get_session_path(self, session_number):
        return self.root_path + str(session_number)

    def get_paths_to_files(self, file_name):
        file_paths = []
        session_paths = self.get_session_paths()

        for i in range(0, len(session_paths)):
            file_path = session_paths[i] + file_name

            if os.path.isfile(file_path):
                file_paths.append(file_path)
            else:
                file_paths.append(None)

        return file_paths
    
    def count_lines_in_files(self, paths_to_files):
        lines_in_files = []

        for i in range(0, len(paths_to_files)):
            file_path = paths_to_files[i]
            if file_path != None and os.path.isfile(file_path):
                file_to_count = open(file_path,'r')
                file_content = file_to_count.read()
                number_of_lines = len(file_content.split("\n"))

                lines_in_files.append(number_of_lines)
                file_to_count.close()
            else:
                lines_in_files.append(0)
        
        return lines_in_files


class SessionDataCollector:
    def __init__(self):
        self.sessions = Sessions('sessions/')

    def session_all_frames_counts(self):
        paths_to_all_frames = self.sessions.get_paths_to_files("/artifacts/all.frames")

        return self.sessions.count_lines_in_files(paths_to_all_frames)

    def session_elka_downlink_frames_counts(self):
        paths_to_elka_downlink_frames = self.sessions.get_paths_to_files("/artifacts/elka_downlink.frames")

        return self.sessions.count_lines_in_files(paths_to_elka_downlink_frames)
    
    def session_fp_gs_downlink_frames_counts(self):
        paths_to_gliwice_downlink_frames = self.sessions.get_paths_to_files("/artifacts/gliwice_downlink.frames")
        paths_to_fp_gs_downlink_frames = self.sessions.get_paths_to_files("/artifacts/fp-gs_downlink.frames")

        gliwice_downlink_frames = self.sessions.count_lines_in_files(paths_to_gliwice_downlink_frames)
        fp_gs_downlink_frames = self.sessions.count_lines_in_files(paths_to_fp_gs_downlink_frames)

        return map(operator.add, fp_gs_downlink_frames, gliwice_downlink_frames)
    
    def number_of_sessions(self):
        return len(self.sessions.get_session_paths())


class NiceSessionPlots:
    PLOT_DPI = 600
    PLOT_BAR_WIDTH = 0.4

    def __init__(self):
        data_collector = SessionDataCollector()

        self.number_of_sessions = data_collector.number_of_sessions()

        self.all_frames = data_collector.session_all_frames_counts()
        self.fp_gs_downlink_frames = data_collector.session_fp_gs_downlink_frames_counts()
        self.elka_downlink_frames = data_collector.session_elka_downlink_frames_counts()

    def plot_all_frames_to_file(self, file_path):
        x = range(1, self.number_of_sessions + 1)

        plt.figure(1)
        plt.title('all.frames vs session number')
        plt.grid(True)
        plt.bar(x, self.all_frames, color='g', label="all.frames")

        plt.xlim(xmin = 1, xmax = len(self.all_frames) + 1)
        plt.ylim(ymin = 0, ymax = max(self.all_frames) + 50)
        plt.xlabel('Session number')
        plt.ylabel('all.frames count')

        plt.legend(bbox_to_anchor=(0.5, 0.98), loc=1, borderaxespad=0., frameon=False)

        plt.savefig(file_path, dpi=self.PLOT_DPI)

    def plot_fp_vs_elka_downlink_frames_to_file(self, file_path):
        x = range(1, self.number_of_sessions + 1)

        plt.figure(2)
        plt.title('elka vs fp-gs downlink.frames vs session number')
        plt.grid(True)
        plt.bar(map(operator.add, x, [-0.2 for i in range(0, len(x))]), self.fp_gs_downlink_frames, self.PLOT_BAR_WIDTH, color='r', label="fp-gs")
        plt.hold(True)
        plt.bar(map(operator.add, x, [0.2 for i in range(0, len(x))]), self.elka_downlink_frames, self.PLOT_BAR_WIDTH, color='b', label="elka")

        plt.xlim(xmin = 1, xmax = len(self.all_frames) + 1)
        plt.ylim(ymin = 0, ymax = max(self.all_frames) + 50)
        plt.xlabel('Session number')
        plt.ylabel('downlink.frames count')

        plt.legend(bbox_to_anchor=(0.5, 0.98), loc=1, borderaxespad=0., frameon=False)

        plt.savefig(file_path, dpi=self.PLOT_DPI)


if __name__ == "__main__":
    session_plots = NiceSessionPlots()

    print "Info: Generating analytics..."

    session_plots.plot_all_frames_to_file("all_frames.png")
    session_plots.plot_fp_vs_elka_downlink_frames_to_file("fp_vs_elka_frames.png")
