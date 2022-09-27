from gemfileparser2 import GemfileParser
import rubygeminfo

gemfile = "/Users/rsitro/dev/chronograph/Gemfile"

def main():
    n = GemfileParser(gemfile, "chronograph")
    dependency_dictionary = n.parse()
    for env, dependencies in dependency_dictionary.items():
        if dependencies:
            print("########################")
            print("------- {} -------".format(env))
            gem_names = []
            for gem in dependencies:
                gem_names.append(gem.name)
            licenses = rubygeminfo.get_licenses(gem_names)
            print(licenses)
            print()


if __name__ == "__main__":
    main()