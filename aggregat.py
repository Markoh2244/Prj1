import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import pyart


aws_nexrad_level2_file = "s3://noaa-nexrad-level2/2022/03/22/KHGX/KHGX20220322_120125_V06"

#######################################
# We can use the **pyart.io.read_nexrad_archive** module to access our data, passing in the filepath.

radar = pyart.io.read_nexrad_archive(aws_nexrad_level2_file)
# # Read the radar data.
# # radar = pyart.io.read("sgpcsaprsurcmacI7.c0.20110520.095101.nc")

# # Store the radar field into a variable.
# ref_field = radar.fields['reflectivity_horizontal']['data'].copy()

# # To create an array that is zero when the condition is false and one when it is true, we
# # can make use of the np.ma.where command.
# ref_gt_0 = np.ma.where(ref_field > 0, 1, 0)
# print(ref_gt_0)

# # To create a new field, we need to create a dictionary with keys containing the data,
# # the long name, the units, the fill value, and the standard name.
# mask_dict = {'data': ref_gt_0, 'units': '0 = Z < 0, 1 = Z >= 0', 'long_name': 'reflectivity_mask',
#              '_FillValue': ref_gt_0.fill_value, 'standard_name': 'reflectivity_mask'}


# # Adding this field into the radar object using radar.add_field()
# radar.add_field('reflectivity_mask', mask_dict, replace_existing=True)


# # Plot the data using RadarMapDisplay
# plt.figure(figsize=[12, 8])
# projection = ccrs.LambertConformal(central_latitude=radar.latitude['data'][0],
#                                    central_longitude=radar.longitude['data'][0])
# display = pyart.graph.RadarMapDisplay(radar)
# display.plot_ppi_map('reflectivity_mask', projection=projection, cmap='coolwarm', vmin=0, vmax=1)

# Writing this radar object to a new file is as simple as using pyart.io.write_cfradial()
print(radar)
print(radar.fields['reflectivity']['data'].shape)
pyart.io.write_cfradial('new_radar.nc', radar)