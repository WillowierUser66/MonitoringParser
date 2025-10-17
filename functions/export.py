def export(data):
    import h5py

    with h5py.File('output/ir_data.h5','w') as hdf:
        hdf.create_dataset('data', data=data, dtype=float)

