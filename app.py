import os

class Permutator:

    def __init__(self, nameFile, outFile, quiet, seperationSymbols=(".", "-", "_", " ", "")):
        self.nameFile = nameFile
        self.outFile = outFile
        self.quiet = quiet
        self.seperationSymbols = seperationSymbols

    def start(self):
        totalProcessed = 0
        if self.outFile is not None and os.path.exists(self.outFile) and os.path.splitext(self.outFile)[-1] == ".txt":
            os.remove(self.outFile)

        if not os.path.exists(self.nameFile):
            self.print(f"Input file does not exist: [{self.nameFile}]")
            exit(1)

        with open(self.nameFile, "r", errors="ignore") as names:
            for name in names.readlines():
                permutations = sorted(list(set(self.permutate(name.strip("\n").split(" ")))),
                                      key=lambda x: (len(x), x),
                                      reverse=True)
                if self.outFile is None:
                    print("\n".join(permutations))

                elif self.outFile is not None:
                    with open(self.outFile, "a+") as f:
                        f.write("\n".join(permutations)+"\n")
                    totalProcessed += len(permutations)

        print(f"★ Generated {totalProcessed} usernames into {self.outFile}")

    def permutate(self, name):
        if len(name) == 1:
            self.print(f"Single name found: [{name[0]}], skipping...")
            return []
        if len(name) >= 3:
            self.print(f"Names with more than 3 words is not supported yet, violator: [{' '.join(name)}]")
            exit(1)

        # Basic capitalization permutations
        nameSets = [
            [name[0].lower(), name[1].lower()],
            [name[0].capitalize(), name[1].capitalize()],
            [name[0].upper(), name[1].upper()],
        ]
        # Firstname and lastname naming conventions
        for name in nameSets.copy():
            nameSets += [[name[0][0], name[1]]]     # w*hacker
            nameSets += [[name[0], name[1][0]]]     # walter*h
            nameSets += [[name[0][0], name[1][0]]]  # w*h

            # All possible combinations of shortened first or last names
            for x in range(len(name[0])):
                for y in range(len(name[1])):
                    nameSets += [[name[0][:x+1], name[1][:y+1]]]

        # Add the seperators
        for name in nameSets:
            for symbol in self.seperationSymbols:
                yield name[0] + symbol + name[1]

    def print(self, text):
        if not self.quiet:
            print("✸ "+text)

