Name:           ros-hydro-pr2-self-test
Version:        1.0.6
Release:        0%{?dist}
Summary:        ROS pr2_self_test package

Group:          Development/Libraries
License:        TODO
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-joint-qualification-controllers
Requires:       ros-hydro-pr2-bringup-tests
Requires:       ros-hydro-pr2-counterbalance-check
Requires:       ros-hydro-pr2-self-test-msgs
BuildRequires:  ros-hydro-catkin

%description
The pr2_self_test package

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
* Fri Nov 28 2014 Dash <dash@clearpathrobotics.com> - 1.0.6-0
- Autogenerated by Bloom

* Fri Nov 28 2014 Dash <dash@clearpathrobotics.com> - 1.0.5-0
- Autogenerated by Bloom

* Fri Oct 17 2014 Dash <dash@clearpathrobotics.com> - 1.0.3-1
- Autogenerated by Bloom

* Wed Oct 15 2014 Dash <dash@clearpathrobotics.com> - 1.0.3-0
- Autogenerated by Bloom

* Tue Sep 16 2014 marco <marco@todo.todo> - 1.0.2-0
- Autogenerated by Bloom

