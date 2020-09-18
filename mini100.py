import os

def mini100(videopath, minipath,mod='train'):
    with open(videopath, 'r') as video_f:
        all_videos = video_f.readlines()
        #if mod=='train':
        #    count = [400 for _ in range(0,100)]
        #else:
        #    count = [25 for _ in range(0,100)]
        count = [0 for _ in range(0,100)]
        with open(minipath,'w') as f:
            for video in all_videos:
                #print(video)
                path, label = video.split(',')
                label = int(label)
                if label<100:
                    #if count[label]>0:
                    #    count[label] -= 1
                    count[label] +=1
                    
                    f.write(video)
        
        for cls,i in enumerate(count):
            #if i!=0:
            print("{} class have : {}".format(cls,i))
        print("total {}".format(sum(count)))
           # assert i==0

def mini200(videopath, minipath,mod='train'):
    with open(videopath, 'r') as video_f:
        all_videos = video_f.readlines()
        #if mod=='train':
        #    count = [400 for _ in range(0,100)]
        #else:
        #    count = [25 for _ in range(0,100)]
        count = [0 for _ in range(0,200)]
        with open(minipath,'w') as f:
            for video in all_videos:
                #print(video)
                path, label = video.split(',')
                label = int(label)
                if label<200:
                    #if count[label]>0:
                    #    count[label] -= 1
                    count[label] +=1
                    
                    f.write(video)
        
        for cls,i in enumerate(count):
            #if i!=0:
            print("{} class have : {}".format(cls,i))
        print("total {}".format(sum(count)))
           # assert i==0

def exist_or_not(ann,):
    with open(ann, 'r') as f:
        all = f.readlines()
        for video in all:
            path  =video.split(',')[0]
            if not os.path.isfile(path):
                print(path)
    print("all done!")
        
if __name__ == "__main__":
    import fire
    fire.Fire()

