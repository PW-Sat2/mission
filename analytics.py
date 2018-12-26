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

#class NiceSessionPlots:
#    def __init__(self):

print "Info: Generating analytics..."

data_collector = SessionDataCollector()
all_frames = data_collector.session_all_frames_counts()

# Plot to file
x = range(1, data_collector.number_of_sessions() + 1)
bar_width = 0.4

plt.figure(1)
plt.subplot(211)
plt.title('Number of frames vs session number')
plt.grid(True)
plt.bar(x, all_frames, color='g', label="all.frames")

plt.xlim(xmin = 1, xmax = len(all_frames) + 1)
plt.ylim(ymin = 0, ymax = max(all_frames) + 50)
plt.ylabel('all.frames count')

plt.legend(bbox_to_anchor=(0.5, 0.98), loc=1, borderaxespad=0., frameon=False)

plt.subplot(212)
plt.grid(True)
plt.bar(map(operator.add, x, [-0.2 for i in range(0, len(x))]), data_collector.session_fp_gs_downlink_frames_counts(), bar_width, color='r', label="fp-gs")
plt.hold(True)
plt.bar(map(operator.add, x, [0.2 for i in range(0, len(x))]), data_collector.session_elka_downlink_frames_counts(), bar_width, color='b', label="elka")

plt.xlim(xmin = 1, xmax = len(all_frames) + 1)
plt.ylim(ymin = 0, ymax = max(all_frames) + 50)
plt.xlabel('Session number')
plt.ylabel('downlink.frames count')

plt.legend(bbox_to_anchor=(0.5, 0.98), loc=1, borderaxespad=0., frameon=False)

plt.savefig('frames_count.png', dpi=600)
