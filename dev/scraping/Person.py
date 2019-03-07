class Person(object):
    def __init__(self, first_name, last_name, year, major, academic_interests, post_grad_goal, software_experience,
                 hobbies):
        self.first_name = first_name
        self.last_name = last_name
        self.year = self.remap_year(year)
        self.major = self.remap_major(major)
        self.academic_interests = self.remap_academic_interests(academic_interests.split(', '))
        self.post_grad_goal = self.remap_post_grad_goal(post_grad_goal)
        self.software_experience = self.remap_software_experience(software_experience.split(', '))
        self.hobbies = self.remap_hobbies(hobbies.split(', '))

    """
    Data Remapping Functions
    """
    def remap_year(self, orig_value):
        """
        Remaps values from survey education year to year for KB.

        :param orig_value: (string) value to be remapped.
        :return: (string) remapped education year.
        """
        remapping = {
            'Freshman': 'NUUndergraduate',
            'Sophomore': 'NUUndergraduate',
            'Junior': 'NUUndergraduate',
            'Senior': 'NUUndergraduate',
            'Masters Student': 'NUMastersStudent',
            'PhD Student': 'NUPhDStudent',
            'Post-Doc': 'PostDoc'
        }

        return self.remap_single_value(orig_value, remapping)

    def remap_major(self, orig_value):
        """
        Remaps values from survey major to field of study for KB.

        :param orig_value: (string) value to be remapped.
        :return: (string) remapped major.
        """
        remapping = {
            'Computer Science': 'ComputerScience',
            'Cognitive Science': 'CognitiveScience',
            'Masters in AI (MSAI)': 'ArtificialIntelligence',
            'Masters in Robotics (MSR)': 'Robotics',
            'Masters in Analytics (MSiA)': 'Analytics',
            'Other': 'Other'
        }

        return self.remap_single_value(orig_value, remapping)

    def remap_academic_interests(self, orig_values):
        """
        Remaps values from survey academic interests to interests for KB.

        :param orig_values: (list of strings) list of values to be remapped.
        :return: (list of strings) remapped academic interests
        """
        remapping = {
            'Artificial Intelligence (AI)': 'ArtificialIntelligence',
            'Machine Learning (ML)': 'MachineLearning',
            'Human-Computer Interaction (HCI)': 'HumanComputerInteraction',
            'Computer Vision': 'ComputerVision',
            'Game Development': 'GameDevelopment',
            'Graphics': 'Graphics',
            'Robotics': 'Robotics',
            'Networking': 'Networking',
            'Systems': 'ComputerScienceSystems',
            'Computational Theory': 'ComputerScienceTheory'
        }

        return self.remap_list_values(orig_values, remapping)

    def remap_post_grad_goal(self, orig_value):
        """
        Remaps values from survey post-grad goal to goals for KB.

        :param orig_value: (string) value to be remapped.
        :return: (string) remapped post-grad goal.
        """
        remapping = {
            'Software Engineer': 'SoftwareEngineer',
            'Project Manager': 'ProjectManager',
            'Consultant': 'Consultant',
            'Post-Doc': 'PostDoc',
            'Faculty': 'Faculty',
            'Industry Research': 'IndustryResearch',
            'Other': 'Other'
        }

        return self.remap_single_value(orig_value, remapping)

    def remap_software_experience(self, orig_values):
        """
        Remaps values from survey software experience to experience for KB.

        :param orig_values: (list of strings) list of values to be remapped.
        :return: (list of strings) remapped software experience.
        """
        remapping = {
            'Backend web development': 'BackendWeb',
            'Frontend web development': 'FrontendWeb',
            'Game Development': 'GameDevelopment',
            'iOS mobile development': 'iOSDevelopment',
            'Android development': 'AndroidDevelopment',
            'Data Science and Machine Learning': 'DataScience',
            'Hardware (e.g. Arduinos; Raspberry Pi; etc.)': 'Hardware'
        }

        return self.remap_list_values(orig_values, remapping)

    def remap_hobbies(self, orig_values):
        """
        Remaps values from survey hobbies to hobbies for KB.

        :param orig_values: (list of strings) list of values to be remapped.
        :return: (list of strings) remapped hobbies.
        """
        remapping = {
            'Sports': 'Sports',
            'Movies': 'Movies',
            'Traveling': 'Traveling',
            'Art and Culture': 'Art',
            'Music': 'Music',
            'Food': 'Food',
            'Hackathons': 'Hackathons'
        }

        return self.remap_list_values(orig_values, remapping)

    """
    Utility Functions for Remapping
    """
    @staticmethod
    def remap_list_values(orig_values, remapping):
        """
        Remaps values in a list to new values based on remapping dict.

        :param orig_values: (list of strings) list of values to be remapped.
        :param remapping: (dict of strings) remapping from orig_values to new values.
        :return: (list of strings) list of remapped values based on remappings.
        """
        return [remapping[x] if x in remapping else x for x in orig_values]

    @staticmethod
    def remap_single_value(value, remapping):
        """
        Remaps a single value based on remapping dict.

        :param value: (string) string value to be remapped.
        :param remapping: (dict of strings) remapping from orig_values to new values.
        :return: (string) remapped string based on remapping. blank string if not in remapping.
        """
        return remapping[value] if value in remapping else ''

    """
    Output Functions
    """
    def __str__(self):
        """
        Create human-readable string from Person's data
        :return: (string) Person object in human-friendly string.
        """
        output_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'year': self.year,
            'major': self.major,
            'academic_interests': self.academic_interests,
            'post_grad_goal': self.post_grad_goal,
            'software_experience': self.software_experience,
            'hobbies': self.hobbies
        }
        return str(output_dict)

    def generate_krf(self):
        """
        Generates the krf output for this Person to be used with Companion.

        :return: (string) krf output that ontologizes all information about this Person.
        """
        output_list = []

        # create entity
        entity = self.first_name + self.last_name
        output_list += ['(isa {0:} {1:})'.format(entity, self.year)]

        # add full name
        output_list += ['(fullName {0:} {1:})'.format(entity, "\"{0:} {1:}\"".format(self.first_name, self.last_name))]

        # add major
        if self.major != 'Other':
            output_list += ['(studies {0:} {1:})'.format(entity, self.major)]

        # add academic interests
        output_list += ['(academicInterest {0:} {1:})'.format(entity, interest) for interest in self.academic_interests]

        # add post grad goal
        if self.post_grad_goal != 'Other':
            output_list += ['(hasFutureCareer {0:} {1:})'.format(entity, self.post_grad_goal)]

        # add software experience
        output_list += ['(isExperiencedWith {0:} {1:})'.format(entity, skill) for skill in self.software_experience]

        # add hobbies
        output_list += ['(enjoysHobby {0:} {1:})'.format(entity, skill) for skill in self.hobbies]

        return '\n'.join(output_list)
