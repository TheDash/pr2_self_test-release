Name:           ros-hydro-pr2-counterbalance-check
Version:        1.0.5
Release:        0%{?dist}
Summary:        ROS pr2_counterbalance_check package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_counterbalance_check
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-joint-qualification-controllers
Requires:       ros-hydro-pr2-controller-configuration
Requires:       ros-hydro-pr2-controller-manager
Requires:       ros-hydro-pr2-controllers-msgs
Requires:       ros-hydro-pr2-self-test-msgs
Requires:       ros-hydro-rospy
Requires:       ros-hydro-std-msgs
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-joint-qualification-controllers
BuildRequires:  ros-hydro-pr2-controller-configuration
BuildRequires:  ros-hydro-pr2-controller-manager
BuildRequires:  ros-hydro-pr2-controllers-msgs
BuildRequires:  ros-hydro-pr2-self-test-msgs
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-std-msgs

%description
pr2_counterbalance_check

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Nov 28 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.5-0
- Autogenerated by Bloom

* Fri Oct 17 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.3-1
- Autogenerated by Bloom

* Wed Oct 15 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.3-0
- Autogenerated by Bloom

* Tue Sep 16 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.2-0
- Autogenerated by Bloom

