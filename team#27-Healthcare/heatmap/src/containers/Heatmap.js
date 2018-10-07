import React from 'react';
import {
  withScriptjs,
  withGoogleMap,
  GoogleMap,
  Marker,
  InfoWindow
} from 'react-google-maps';
import { SearchBox } from 'react-google-maps/lib/components/places/SearchBox';
import _ from 'lodash';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { compose, withProps } from 'recompose';
import { getAll } from '../redux/reducers/get_data';
import MarkerBlue from '../static/icons/marker-blue.png';
import MarkerRed from '../static/icons/marker-red.png';
import MarkerYellow from '../static/icons/marker-yellow.png';
import MarkerGreen from '../static/icons/marker-green.png';
import MarkerPurple from '../static/icons/marker-purple.png';
import MarkerBlue64 from '../static/icons/marker-blue-64.png';
import MarkerRed64 from '../static/icons/marker-red-64.png';
import MarkerYellow64 from '../static/icons/marker-yellow-64.png';
import MarkerGreen64 from '../static/icons/marker-green-64.png';
import MarkerPurple64 from '../static/icons/marker-purple-64.png';
import data from '../static/mockJSON';
import center from '../static/mockCenter';

const marker = {
  flu: {
    name: 'Flu',
    marker: MarkerRed,
    marker64: MarkerRed64
  },
  dengue: {
    name: 'Dengue',
    marker: MarkerBlue,
    marker64: MarkerBlue64
  },
  ebola: {
    name: 'Ebola',
    marker: MarkerYellow,
    marker64: MarkerYellow64
  },
  lyphoma: {
    name: 'Lyphoma',
    marker: MarkerGreen,
    marker64: MarkerGreen64
  },
  malaria: {
    name: 'Malaria',
    marker: MarkerPurple,
    marker64: MarkerPurple64
  }
};

class Heatmap extends React.Component {
  componentWillMount() {
    this.props.actions.getAll();

    const refs = {};

    this.setState({
      bounds: null,
      center: {
        lat: 41.9,
        lng: -87.624
      },
      markers: [],
      onMapMounted: ref => {
        refs.map = ref;
      },
      onBoundsChanged: () => {
        this.setState({
          bounds: refs.map.getBounds(),
          center: refs.map.getCenter()
        });
      },
      onSearchBoxMounted: ref => {
        refs.searchBox = ref;
      },
      onPlacesChanged: () => {
        const places = refs.searchBox.getPlaces();
        const bounds = new window.google.maps.LatLngBounds();

        places.forEach(place => {
          if (place.geometry.viewport) {
            bounds.union(place.geometry.viewport);
          } else {
            bounds.extend(place.geometry.location);
          }
        });
        const nextMarkers = places.map(place => ({
          position: place.geometry.location
        }));
        const nextCenter = _.get(nextMarkers, '0.position', this.state.center);

        this.setState({
          center: nextCenter,
          markers: nextMarkers
        });
        // refs.map.fitBounds(bounds);
      }
    });
  }
  render() {
    console.log(19, this.props);
    console.log(43, this.state);

    return (
      <GoogleMap
        defaultZoom={5}
        // defaultCenter={{ lat: 43.30560543382353, lng: -95.50891406589727 }}
        defaultCenter={this.state.center}
      >
        {this.props.isMarkerShown && (
          <React.Fragment>
            <React.Fragment>
              {Object.keys(marker).map(dea => (
                <div key={dea}>
                  {data[dea].map((latlong, index) => (
                    <Marker
                      key={`${index}+${latlong[0]}`}
                      icon={{
                        url: marker[dea].marker
                      }}
                      position={{ lat: latlong[0], lng: latlong[1] }}
                    >
                      {/* <InfoWindow>
                <div style={{ color: 'black' }}>Infowindow texte</div>
              </InfoWindow> */}
                    </Marker>
                  ))}
                </div>
              ))}
            </React.Fragment>
            <React.Fragment>
              {Object.keys(marker).map(dea => (
                <div key={dea}>
                  {center[dea][0].map((latlong, index) => (
                    <div>
                      {center[dea][1][index] >= 5 && (
                        <Marker
                          key={`${index}+${latlong[0]}`}
                          icon={{
                            url: marker[dea].marker64
                          }}
                          position={{ lat: latlong[0], lng: latlong[1] }}
                        >
                          {/* <InfoWindow>
                <div style={{ color: 'black' }}>Infowindow texte</div>
              </InfoWindow> */}
                        </Marker>
                      )}
                    </div>
                  ))}
                </div>
              ))}
            </React.Fragment>
          </React.Fragment>
        )}

        <SearchBox
          ref={this.state.onSearchBoxMounted}
          bounds={this.state.bounds}
          controlPosition={window.google.maps.ControlPosition.TOP_CENTER}
          onPlacesChanged={this.state.onPlacesChanged}
        >
          <input
            type="text"
            placeholder="Enter the location"
            style={{
              boxSizing: `border-box`,
              border: `1px solid transparent`,
              width: `240px`,
              height: `32px`,
              marginTop: `27px`,
              padding: `0 12px`,
              borderRadius: `3px`,
              boxShadow: `0 2px 6px #0864c1`,
              fontSize: `14px`,
              outline: `none`,
              textOverflow: `ellipses`
            }}
          />
        </SearchBox>
        {/* {this.props.markers.map((marker, index) => (
          <Marker key={index} position={marker.position} />
        ))} */}
      </GoogleMap>
    );
  }
}

const mapStateToProps = state => ({
  state
});

const mapDispatchToProps = dispatch => ({
  actions: bindActionCreators(
    {
      getAll
    },
    dispatch
  ),
  dispatch
});

export default compose(
  withProps({
    googleMapURL:
      'https://maps.googleapis.com/maps/api/js?key=AIzaSyAulodcRp7D6_M_5qsQm32hppHb20VRFdk&v=3.exp&libraries=geometry,drawing,places',
    loadingElement: <div style={{ height: `100%` }} />,
    containerElement: <div style={{ height: `970px` }} />,
    mapElement: <div style={{ height: `100%` }} />
  }),
  withScriptjs,
  withGoogleMap,
  connect(
    mapStateToProps,
    mapDispatchToProps
  )
)(Heatmap);
