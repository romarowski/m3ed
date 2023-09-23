from eventpy.dataloader import DataLoader

def main():
    filename = '/home/ben/penn/grasp/m3ed/output/car_urban_day_horse_data.h5'
    dataloader = DataLoader(filename=filename)
    dataloader.load_events(timestamp=0)

    pass

if __name__ == '__main__':
    main()

