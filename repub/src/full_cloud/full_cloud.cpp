#include <pcl_conversions/pcl_conversions.h>
#include <sensor_msgs/PointCloud2.h>

typedef pcl::PointXYZINormal PointType;
typedef pcl::PointCloud<PointType> PointCloudXYZI;
int tot;
void cloudCB(const sensor_msgs::PointCloud2 &input)
{
    pcl::PointCloud<PointType> cloud;
    pcl::fromROSMsg(input, cloud);

    std::stringstream ss;
    ss << std::setw(4) << std::setfill('0') << tot++;
	std::string pcd_path;
	ss >> pcd_path;
    pcd_path = "/root/soft/livox/data/full_pcd/" + pcd_path + ".pcd";
    pcl::io::savePCDFileASCII (pcd_path, cloud);
}
main (int argc, char **argv)
{
    ros::init (argc, argv, "full_cloud");

    ros::NodeHandle nh;
    ros::Subscriber bat_sub = nh.subscribe("/livox_full_cloud_mapped", 1000, cloudCB);

    ros::spin();
    return 0;
}
